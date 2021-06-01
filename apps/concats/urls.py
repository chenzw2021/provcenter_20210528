from django.urls import path
from .views import ConcatView


urlpatterns = [
    path('concat/', ConcatView.as_view()),
]