from django.shortcuts import render
from HomePage.settings import defaultStatus


currentStatus = defaultStatus.copy()
currentStatus['statusHotStuff'] = 'activeCustom'


def hotStuff(request):

	return render(request, 'hotStuff/hotStuff.html', currentStatus)
	