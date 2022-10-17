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
        data: {email: "admin@admin.com", pin: 123123}
    '''

    template_mail_invite = "send-otp.html"
    context = {
        "pin_code": data.get('pin'),
        "full_name": data.get('email').split('@')[0],
    }
    content = render_to_string(template_mail_invite, context)
    send_mail(
        subject="OTP CODE",
        message=f"OTP CODE",
        html_message=content,
        from_email=settings.FROM_EMAIL,
        recipient_list=[data.get('email')],
        fail_silently=False,
    )

    logger.info(f"message from ss: {data.get('email')}")


@app.task()
def send_feedback_by_email(data):
    '''
    arg:
        data: {title: "admin@admin.com", content: 123123}
    '''

    template_mail_invite = "feedback.html"
    context = {
        "title": data.get('title'),
        "content": data.get('content'),
    }
    content = render_to_string(template_mail_invite, context)
    send_mail(
        subject="FEEDBACK",
        message=f"title: {data.get('title')} - content: {data.get('content')}",
        html_message=content,
        from_email=settings.FROM_EMAIL,
        recipient_list=[data.get('email')],
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

    template_mail_invite = "report-grade.html"

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
        "full_name": data.get('full_name'),
    }
    content = render_to_string(template_mail_invite, context)
    send_mail(
        subject="REPORT CARD",
        message=f"REPORT CARD",
        html_message=content,
        from_email=settings.FROM_EMAIL,
        recipient_list=[data.get('email')],
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
        "list_time_table_res": data.get('list_time_table_res', []),
    }
    content = render_to_string(template_mail_invite, context)
    send_mail(
        subject="Info revision",
        message=f"Info revision",
        html_message=content,
        from_email=settings.FROM_EMAIL,
        recipient_list=[data.get('email')],
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

        logger.info(f"start push notification")
        for token in all_token:
            if token is not None:
                PushNotificationHandle().send_push_message(token, title, message, extra=extra)
                logger.info(f"pushed to token: {token}")
        logger.info(f"end push notification")
    else:
        for id in user_id:
            all_token = DeviceTokenPushNotification.objects.filter(
                active=1,
                user_id=id
            ).values_list('token', flat=True)

            logger.info(f"start push notification")
            for token in all_token:
                if token is not None:
                    PushNotificationHandle().send_push_message(token, title, message, extra=extra)
                    logger.info(f"pushed to token: {token}")
            logger.info(f"end push notification")


@app.task()
def notification_chat_celery(input_data):
    '''
    send notification for chat module
    arg:
        data:  {
            title: str
            content: str
            data: str
            user_ids: list[int]
        }
    '''
    title = input_data.get('title')
    content = input_data.get('content')
    user_ids = input_data.get('user_ids')
    data = input_data.get('data')
    if not isinstance(user_ids, list):
        all_token = DeviceTokenPushNotification.objects.filter(
            active=1,
            user_id=user_ids
        ).values_list('token', flat=True)

        logger.info(f"start push notification")
        for token in all_token:
            if token is not None:
                PushNotificationHandle().send_push_message(token, title, content, extra={"data": data})
        logger.info(f"end push notification")
    else:
        for id in user_ids:
            all_token = DeviceTokenPushNotification.objects.filter(
                active=1,
                user_id=id
            ).values_list('token', flat=True)

            logger.info(f"start push notification")
            for token in all_token:
                if token is not None:
                    PushNotificationHandle().send_push_message(token, title, content, extra={"data": data})
            logger.info(f"end push notification")


"""
@app.task()
def test_send_message_chat(context):
    from channels.layers import get_channel_layer
    from django.conf import settings

    channel_layer = get_channel_layer()
    from asgiref.sync import async_to_sync

    logger.info(f"start async_to_sync")
    async_to_sync(channel_layer.group_send)(settings.CHANNEL_CHAT_REDIS, context)
    logger.info(f"end async_to_sync")
"""
