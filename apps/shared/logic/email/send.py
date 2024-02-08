from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def send_email(message):
    subject = 'Заявка'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.XDEV_EMAIL, ]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse('Email sent successfully')