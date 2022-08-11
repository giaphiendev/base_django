import logging
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

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


@app.task()
def send_feedback_by_email(data):
    '''
    arg:
        data: {title: "admin@admin.com", content: 123123}
    '''
    logger.info(f"Start send feed")
    send_mail(
        subject=data.get('title', "title"),
        message=data.get('content', "content"),
        from_email=settings.FROM_EMAIL,
        recipient_list=[data.get('title', "hienaloso98@gmail.com")],
        fail_silently=False,
    )
    logger.info(f"Send feed successful!")


@app.task()
def send_report_mark(data):
    '''
    send report about mark
    arg:
        data: {email: "admin@admin.com", **data}
    '''

    template_mail_invite = "info-class.html"
    context = {
        "invitation_url": 'invitation_url',
        "logo_url": 'logo_url',
    }
    content = render_to_string(template_mail_invite, context)
    send_mail(
        subject="Invite",
        message=f"message",
        html_message=content,
        from_email=settings.FROM_EMAIL,
        recipient_list=[data.get('email', "hienaloso98@gmail.com")],
        fail_silently=False,
    )
