from django.urls import path
from .views import PyRedis


urlpatterns = [
    path('redis/', PyRedis.as_view()),
]