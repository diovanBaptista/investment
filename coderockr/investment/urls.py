from django.contrib import admin
from django.urls import path
from investment.views import hello_world
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('investment/', include('investment.urls')),
]