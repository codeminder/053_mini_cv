
from django.urls import path

from .views import *



urlpatterns = [
    path('', cv, name = "cv_home"),
]

