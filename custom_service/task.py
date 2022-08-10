import logging
from django.conf import settings
from django.core.mail import send_mail

from config.celery import app

logger = logging.getLogger("django")


@app.task()
def send_email_from_celery(data):
    '''
    arg:
        data: {mail: "admin@admin.com", pin: 123123}
    '''
    logger.info(f"message from logger: {data.get('pin')}")
    send_mail(
        subject="PIN CODE",
        message=f"Here is your OTP {data.get('pin')} to sign up",
        from_email=settings.FROM_EMAIL,
        recipient_list=[data.get("email")],
        fail_silently=False,
    )
    logger.info(f"message from ss: {data.get('email')}")
