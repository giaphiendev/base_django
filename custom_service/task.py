import logging
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from config.celery import app
from custom_service.handlers.push_notification import PushNotificationHandle
from custom_service.models.ModelTechwiz import DeviceTokenPushNotification
from utils.helper import cal_avg_grade, cal_gpa

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

    data_term1 = data.get('term1')
    data_term2 = data.get('term2')

    for index, item in enumerate(data_term1):
        data_term1[index]['AVG'] = cal_avg_grade(item)

    for index, item in enumerate(data_term2):
        data_term2[index]['AVG'] = cal_avg_grade(item)

    context = {
        "term1": data_term1,
        "term2": data_term2,
        "gpa1": cal_gpa(data_term1),
        "gpa2": cal_gpa(data_term2),
    }
    content = render_to_string(template_mail_invite, context)
    send_mail(
        subject="REPORT CARD",
        message=f"REPORT CARD",
        html_message=content,
        from_email=settings.FROM_EMAIL,
        recipient_list=[data.get('email', "hienaloso98@gmail.com")],
        fail_silently=False,
    )
    logger.info(f"Send email about report card")


@app.task()
def send_info_revision_class(data):
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
    logger.info(f"Send email about report card")


@app.task()
def send_notification_to_device_celery(data):
    '''
    send report about mark
    arg:
        data: {message: "message", extra: {}, user_id: 1}
    '''
    title = data.get('title')
    message = data.get('message')
    extra = data.get('extra')
    user_id = data.get('user_id')
    if not isinstance(user_id, list):
        all_token = DeviceTokenPushNotification.objects.filter(
            active=1,
            user_id=user_id
        ).values_list('token', flat=True)

        for token in all_token:
            logger.info(f"start push notification: {token}")
            PushNotificationHandle().send_push_message(token, title, message, extra=extra)
        logger.info(f"end push notification: ")
    else:
        for id in user_id:
            all_token = DeviceTokenPushNotification.objects.filter(
                active=1,
                user_id=id
            ).values_list('token', flat=True)

            for token in all_token:
                logger.info(f"start push notification: {token}")
                PushNotificationHandle().send_push_message(token, title, message, extra=extra)
            logger.info(f"end push notification: ")
