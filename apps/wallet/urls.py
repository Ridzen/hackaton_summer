from rest_framework.routers import DefaultRouter as DR

from apps.wallet.views import WalletViewSet

router = DR()
router.register('wallet', WalletViewSet, basename='wallets')

urlpatterns = [

]

urlpatterns += router.urls
