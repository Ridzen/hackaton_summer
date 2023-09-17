from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


class EmailVerificationManager:
    def send_verification_email(self, user, request, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        host = request.get_host().split(':')[0]
        port = 443 if request.is_secure() else 80
        verification_link = f"{protocol}{host}:{port}{reverse('verify-email', args=[token])}"

        send_mail(
            'Подтвердите свой email',
            f'Для завершения регистрации перейдите по ссылке: {verification_link}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
