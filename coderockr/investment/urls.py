from os import name
from django.urls import path, include
from rest_framework import routers
from .viewsets import InvestimentationViewSet, WithdrawViewSet, InvestorViewSet
from .viewsets import WithdrawViewSet

api_investment = routers.DefaultRouter()

api_investment.register(
    'investment',
    InvestimentationViewSet,
    basename='investment'
)

api_investment.register(
    'withdraw',
    WithdrawViewSet,
    basename='withdraw'
)

api_investment.register(
    'investor',
    InvestorViewSet,
    basename='investor'
)

urlpatterns = [
    path('investment/', include(api_investment.urls)),
]