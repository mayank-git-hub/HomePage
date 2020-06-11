from django.urls import path

from .views import *

urlpatterns = [
    path('', research, name="research"),
    path('VoiceSeparation', VoiceSeparation, name="VoiceSeparation"),
    path('GraphConvolution', GraphConvolution, name="GraphConvolution"),
]
