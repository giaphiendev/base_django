from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from core.models import User, UserLogEntry
from core.users.utils import normalize_email_address
from utils.validators import password_validation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "phone", "first_name", "last_name", "username", "id")
        extra_kwargs = {
            "id": {"read_only": True},
        }


class RegisterSerializer(serializers.Serializer):
    family_name = serializers.CharField(max_length=150)
    given_name = serializers.CharField(max_length=150)
    email = serializers.EmailField(
        help_text="The email address is also going to be the username."
    )
    password = serializers.CharField(validators=[password_validation])
    authenticate = serializers.BooleanField(
        required=False,
        default=False,
        help_text="Indicates whether an authentication token should be generated and "
                  "be included in the response.",
    )

class ChangePasswordBodyValidationSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField(validators=[password_validation])


class ResetPasswordBodyValidationSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField(validators=[password_validation])



class SendResetPasswordEmailBodyValidationSerializer(serializers.Serializer):
    email = serializers.EmailField(
        help_text="The email address of the user that has requested a password reset."
    )
    base_url = serializers.URLField(
        help_text="The base URL where the user can reset his password. The reset "
                  "token is going to be appended to the base_url (base_url "
                  "'/token')."
    )



class NormalizedEmailField(serializers.EmailField):
    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return normalize_email_address(data)


class NormalizedEmailWebTokenSerializer(JSONWebTokenSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = NormalizedEmailField()

    def validate(self, attrs):
        """
        This serializer is only used by the ObtainJSONWebToken view which is only used
        to generate a new token. When that happens we want to update the user's last
        login timestamp.
        """

        # In the future, when migrating away from the JWT implementation, we want to
        # respond with machine readable error codes when authentication fails.
        validated_data = super().validate(attrs)

        user = validated_data["user"]
        if not user.is_active:
            msg = "User account is disabled."
            raise serializers.ValidationError(msg)

        update_last_login(None, user)
        UserLogEntry.objects.create(actor=user, action="SIGNED_IN")
        # Call the user_signed_in method for each plugin that is un the registry to
        # notify all plugins that a user has signed in.
        from core.registries import plugin_registry

        for plugin in plugin_registry.registry.values():
            plugin.user_signed_in(user)
        return validated_data
