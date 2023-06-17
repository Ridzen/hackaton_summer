from django.utils.translation import gettext_lazy as __


# Статусы для платежа
PAYMENT_CHOICES = (
    ('CREATED', __('STATUS_CREATED')),
    ('PROCESS', __('STATUS_PROCESS')),
    ('SUCCESS', __('STATUS_SUCCESS')),
    ('ROLLBACK', __('STATUS_ROLLBACK')),
)
