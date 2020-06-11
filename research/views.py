from django.shortcuts import render
from HomePage.settings import defaultStatus


currentStatus = defaultStatus.copy()
currentStatus['statusResearch'] = 'activeCustom'


def research(request):

	return render(request, 'research/research.html', currentStatus)


def VoiceSeparation(request):

	return render(request, 'research/VoiceSeparation.html', currentStatus)


def GraphConvolution(request):

	return render(request, 'research/GraphConvolution.html', currentStatus)
