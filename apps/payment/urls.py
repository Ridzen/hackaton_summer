from rest_framework.routers import DefaultRouter as DR

from apps.payment.views import PaymentView


router = DR()
router.register("payment", PaymentView, basename="payment")

urlpatterns = []

urlpatterns += router.urls
