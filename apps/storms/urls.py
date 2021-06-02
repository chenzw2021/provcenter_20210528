from django.urls import path
from .views import StormProjectView


urlpatterns = [
    path('storm/', StormProjectView.as_view()),
]