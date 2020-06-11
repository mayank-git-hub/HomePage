from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('profile', profile, name="profile"),
    path('publications', publications, name="publications"),
	# path('Audio_Source_Separation', Audio_Source_Separation, name="Audio_Source_Separation"),
	# path('Hyperspectral', Hyperspectral, name='Hyperspectral'),
	# path('IDRiD', IDRiD, name='IDRiD'),
	# path('Image_Stitching', Image_Stitching, name='Image_Stitching'),
	# path('ping_pong', ping_pong, name='ping_pong'),
	# path('Resume', Resume, name='Resume'),
	# path('RSA', RSA, name='RSA'),
	# path('Socket', Socket, name='Socket'),
	# path('Text_Detection_CRAFT', Text_Detection_CRAFT, name='Text_Detection_CRAFT'),
	# path('Text_Detection_Pixel_Link', Text_Detection_Pixel_Link, name='Text_Detection_Pixel_Link'),
	# path('YOLO', YOLO, name='YOLO'),
]
