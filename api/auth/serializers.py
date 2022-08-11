from django.db import IntegrityError
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.errors import (
    ERROR_INVALID_PIN,
    ERROR_USER_NOT_FOUND,
    PIN_EXPIRED,
    PIN_NOT_EXISTS
)
from core.decorators import map_exceptions
from core.exceptions import (
    InvalidPin,
    UserNotFound,
    PinNotExists,
    PinExpired
)
from core.models import User
from core.users.handler import UserHandler
from utils import error
from utils.logger import logger_raise_warn_exception


class GetAllFieldUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
            "last_accessed_at": {"write_only": True},
            "is_superuser": {"write_only": True},
            "is_staff": {"write_only": True},
            "groups": {"write_only": True},
            "user_permissions": {"write_only": True},
        }


class CustomizeTokenObtainPairPatchedSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"] = serializers.EmailField()
        # self.fields["pin"] = serializers.IntegerField()
        # self.fields["token"] = serializers.CharField()
        del self.fields['username']
        # del self.fields['password']

    @map_exceptions(
        {
            InvalidPin: ERROR_INVALID_PIN,
            UserNotFound: ERROR_USER_NOT_FOUND,
            PinNotExists: PIN_NOT_EXISTS,
            PinExpired: PIN_EXPIRED
        }
    )
    def validate(self, request_data):
        user = UserHandler().get_user_by_password(request_data)
        refresh = self.get_token(user)

        return {
            "success": True,
            "data": {
                "user": GetAllFieldUserSerializer(user).data,
                "refresh": str(refresh),
                "refresh_expired": refresh.current_time + refresh.lifetime,
                "access": str(refresh.access_token),
                "access_token_expired": refresh.current_time + refresh.access_token.lifetime,
            },
        }


class CustomerSignupSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"] = serializers.EmailField()
        # self.fields["pin"] = serializers.IntegerField()
        # self.fields["token"] = serializers.CharField()
        self.fields["first_name"] = serializers.CharField()
        self.fields["last_name"] = serializers.CharField()

        del self.fields['username']
        # del self.fields['password']

    def validate(self, attrs):
        # pin = UserHandler().get_pin(attrs)
        required_fields = ['email', 'password', 'first_name', 'last_name']
        for field in required_fields:
            if self.initial_data.get(field, None) is None:
                logger_raise_warn_exception(field, error.RequireValue, detail=f"{field} is require")
            attrs[f'{field}'] = self.initial_data.get(field)
        # attrs['pin_object'] = pin
        return attrs

    def create(self, validated_data, **kwargs):
        email = validated_data.get('email')
        username = email.split("@")[0]
        try:
            user = User.objects.create(
                email=email,
                first_name=validated_data.get('first_name'),
                last_name=validated_data.get('last_name'),
                username=username,
                password=validated_data.get('password'),
            )
        except IntegrityError:
            user = User.objects.get(email=email)

        # pin_object = validated_data.get('pin_object')
        # pin_object.user = user
        refresh = self.get_token(user)
        # pin_object.save()

        # try:
        #     UserRole.objects.create(
        #         user=user,
        #         role=Role.objects.get(name=RoleName.CUSTOMER),
        #         is_active=True,
        #     )
        # except Role.DoesNotExist:
        #     raise RoleNotFound("The role is not exit")
        return {
            "refresh": str(refresh),
            "refresh_expired": refresh.current_time + refresh.lifetime,
            "access_token": str(refresh.access_token),
            "access_token_expired": refresh.current_time + refresh.access_token.lifetime,
        }


class CustomerAccountSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200)
    phone = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
