from django.urls import path, include
from .views import BalacneAPI, PaymentAPI
from rest_framework import routers


urlpatterns = [
    path('organizations/<str:inn>/balance/', BalacneAPI.as_view(), name='organization-balance'),
    path('webhook/bank/', PaymentAPI.as_view(), name='organization-balance'),

]
