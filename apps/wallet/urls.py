from django.urls import path

from apps.wallet.views import WalletViewSet, WalletUpdateViewSet


urlpatterns = [
    path('wallet/', WalletViewSet.as_view(), name='wallet'),
    path('wallet/<int:pk>/', WalletUpdateViewSet.as_view(), name='wallet-update'),
]
