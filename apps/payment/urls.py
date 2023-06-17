from rest_framework.routers import DefaultRouter as DR

from apps.payment.views import PaymentView, PaymentFinishView, PaymentRollbackView


router = DR()
router.register("payment", PaymentView, basename="payment")
router.register("payment-finish", PaymentFinishView, basename="payment-finish")
router.register("payment-rollback", PaymentRollbackView, basename="payment-rollback")

urlpatterns = []

urlpatterns += router.urls
