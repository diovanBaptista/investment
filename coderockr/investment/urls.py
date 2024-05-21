from os import name
from django.urls import path, include
from rest_framework import routers
from .viewsets import InvestimentationViewSet

api_investment = routers.DefaultRouter()

api_investment.register(
    'investment',
    InvestimentationViewSet,
    basename='investment'
)

urlpatterns = [
    path('investment/', include(api_investment.urls)),
]