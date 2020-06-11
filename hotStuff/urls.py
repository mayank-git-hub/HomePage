from django.urls import path

from .views import *

urlpatterns = [
    path('', hotStuff, name="hotStuff"),
]
