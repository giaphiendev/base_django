from rest_framework import status, generics, exceptions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from api.auth.serializers import (CustomizeTokenObtainPairPatchedSerializer, CustomerSignupSerializer)
from api.errors import CUSTOMER_ROLE_NOT_EXIT, PIN_EXPIRED, PIN_NOT_EXISTS
from core.constants import ResultStatus
from core.decorators import map_exceptions
from core.exceptions import RoleNotFound, PinNotExists, PinExpired
from core.models import UserPin
from core.users.handler import UserHandler
from custom_service.task import send_email_from_celery


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomizeTokenObtainPairPatchedSerializer


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        token = request.data.get("refresh_token")
        UserHandler().logout_customer(token)
        return Response({"revoked": request.data.get("refresh_token")}, status=200)


class CustomRefreshToken(TokenRefreshView):
    """
       Takes a refresh type JSON web token and returns an access type JSON web
       token if the refresh token is valid.
       body: {refresh: 'refresh_token_here'}
    """


class CustomSignupPinView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        pin = UserPin().generate_pin_sign_up()
        send_email_from_celery.delay(pin.code)
        response = {"result": "success", "payload": {"token": str(pin.device_token)}, "errors": None}
        return Response(response, status=200)


class CustomSignupView(TokenObtainPairView, generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CustomerSignupSerializer

    @map_exceptions(
        {
            PinExpired: PIN_EXPIRED,
            PinNotExists: PIN_NOT_EXISTS,
            RoleNotFound: CUSTOMER_ROLE_NOT_EXIT,
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            payload = serializer.save()
            data = {
                "result": ResultStatus.SUCCESS,
                "payload": payload,
                "errors": None
            }
            return Response(data, status=status.HTTP_201_CREATED)
        raise exceptions.APIException()
