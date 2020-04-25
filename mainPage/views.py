from django.shortcuts import render

# Create your views here.

def index(request):

	return render(request, 'homepage/index.html')

def Audio_Source_Separation(request):

	return render(request, 'homepage/Audio_Source_Separation.html')

def Hyperspectral(request):

	return render(request, 'homepage/Hyperspectral.html')

def IDRiD(request):

	return render(request, 'homepage/IDRiD.html')

def Image_Stitching(request):

	return render(request, 'homepage/Image_Stitching.html')

def ping_pong(request):

	return render(request, 'homepage/ping_pong.html')

def Resume(request):

	return render(request, 'homepage/Resume.html')

def RSA(request):

	return render(request, 'homepage/RSA.html')

def Socket(request):

	return render(request, 'homepage/Socket.html')

def Text_Detection_CRAFT(request):

	return render(request, 'homepage/Text_Detection_CRAFT.html')

def Text_Detection_Pixel_Link(request):

	return render(request, 'homepage/Text_Detection_Pixel_Link.html')

def YOLO(request):

	return render(request, 'homepage/YOLO.html')