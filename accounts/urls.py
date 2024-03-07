from django.urls import path
from .views import check_oauth

urlpatterns = [
    path('check_oauth/', check_oauth, name='check_oauth'),
]
