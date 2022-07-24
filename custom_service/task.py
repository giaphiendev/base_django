import logging
from time import sleep

from config.celery import app

logger = logging.getLogger("django")


@app.task()
def send_email_from_celery(message):
    sleep(5)
    logger.info(f'message from logger: {message}')
    # send_mail(
    #     subject="PIN CODE",
    #     message=f"Here is your OTP {pin.code} to sign up",
    #     from_email=settings.FROM_EMAIL,
    #     recipient_list=[request.GET.get("email")],
    #     fail_silently=False,
    # )
