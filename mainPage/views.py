from django.shortcuts import render
from HomePage.settings import defaultStatus


def index(request):

	currentStatus = defaultStatus.copy()
	currentStatus['statusHome'] = 'activeCustom'

	return render(request, 'homepage/index.html', currentStatus)


def profile(request):

	currentStatus = defaultStatus.copy()
	currentStatus['statusProfile'] = 'activeCustom'

	return render(request, 'homepage/profile.html', currentStatus)


def publications(request):

	currentStatus = defaultStatus.copy()
	currentStatus['statusPublications'] = 'activeCustom'

	return render(request, 'homepage/publications.html', currentStatus)


# def Audio_Source_Separation(request):

# 	return render(request, 'homepage/Audio_Source_Separation.html')

# def Hyperspectral(request):

# 	return render(request, 'homepage/Hyperspectral.html')

# def IDRiD(request):

# 	return render(request, 'homepage/IDRiD.html')

# def Image_Stitching(request):

# 	return render(request, 'homepage/Image_Stitching.html')

# def ping_pong(request):

# 	return render(request, 'homepage/ping_pong.html')

# def Resume(request):

# 	return render(request, 'homepage/Resume.html')

# def RSA(request):

# 	return render(request, 'homepage/RSA.html')

# def Socket(request):

# 	return render(request, 'homepage/Socket.html')

# def Text_Detection_CRAFT(request):

# 	return render(request, 'homepage/Text_Detection_CRAFT.html')

# def Text_Detection_Pixel_Link(request):

# 	return render(request, 'homepage/Text_Detection_Pixel_Link.html')

# def YOLO(request):

# 	return render(request, 'homepage/YOLO.html')