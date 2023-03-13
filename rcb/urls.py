from rcb.views import *
from django.urls import path
app_name='teamone'
urlpatterns=[
    path('kohli/',kohli,name='kohli'),
]