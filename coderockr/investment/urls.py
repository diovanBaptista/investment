from django.urls import path, include
from rest_framework import routers
from .viewsets import InvestimentationViewSet, WithdrawViewSet, InvestorViewSet
from .viewsets import WithdrawViewSet

api_investment = routers.DefaultRouter()
api_investor = routers.DefaultRouter()
api_withdraw = routers.DefaultRouter()

api_investment.register(
    'investment',
    InvestimentationViewSet,
    basename='investment'
)

api_withdraw.register(
    'withdraw',
    WithdrawViewSet,
    basename='withdraw'
)

api_investor.register(
    'investor',
    InvestorViewSet,
    basename='investor'
)

urlpatterns = [
    path('investment/', include(api_investment.urls)),
    path('withdraw/', include(api_withdraw.urls)),
    path('investor/', include(api_investor.urls)),
]