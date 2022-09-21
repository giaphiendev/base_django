from custom_service.models.ModelTechwiz import DeviceTokenPushNotification
from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError, PushTicketError,
)
import rollbar
from requests.exceptions import ConnectionError, HTTPError
import logging

logger = logging.getLogger("django")


class PushNotificationHandle:
    def add_push_notification_token(self, user, data):
        '''
        arg:
            data: {token: 'abcxyz'}
        return:
        '''
        device, created = DeviceTokenPushNotification.objects.get_or_create(token=data.get('token'), user=user)

        return device

    # Basic arguments. You should extend this function with the push features you
    # want to use, or simply pass in a `PushMessage` object.
    def send_push_message(self, token, title, message, extra=None):
        try:
            push_message = PushMessage(
                to=token,
                title=title,
                body=message,
                data=extra
            )
            response = PushClient().publish(push_message)
            logger.info(f"push_message: {push_message}")
        except PushServerError as exc:
            # Encountered some likely formatting/validation error.
            rollbar.report_exc_info(
                extra_data={
                    'token': token,
                    'message': message,
                    'extra': extra,
                    'errors': exc.errors,
                    'response_data': exc.response_data,
                })
            logger.error(f"PushServerError: ", {
                    'token': token,
                    'message': message,
                    'extra': extra,
                    'errors': exc.errors,
                    'response_data': exc.response_data,
                })
            raise
        except (ConnectionError, HTTPError) as exc:
            # Encountered some Connection or HTTP error - retry a few times in
            # case it is transient.
            rollbar.report_exc_info(
                extra_data={'token': token, 'message': message, 'extra': extra})

            logger.error(f"ConnectionError, HTTPError: ", exc)
            raise self.retry(exc=exc)

        try:
            # We got a response back, but we don't know whether it's an error yet.
            # This call raises errors so we can handle them with normal exception
            # flows.
            response.validate_response()
            logger.info(f"validate_response ss")
        except DeviceNotRegisteredError:
            # Mark the push token as inactive
            DeviceTokenPushNotification.objects.filter(token=token).update(active=False)
            logger.error(f"DeviceNotRegisteredError")
        except PushTicketError as exc:
            # Encountered some other per-notification error.
            rollbar.report_exc_info(
                extra_data={
                    'token': token,
                    'message': message,
                    'extra': extra,
                    'push_response': exc.push_response._asdict(),
                })
            logger.error(f"PushTicketError: {exc}")
            raise self.retry(exc=exc)
