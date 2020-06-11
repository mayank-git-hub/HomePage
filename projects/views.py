from django.shortcuts import render
from HomePage.settings import defaultStatus


currentStatus = defaultStatus.copy()
currentStatus['statusProjects'] = 'activeCustom'


def projects(request):

	return render(request, 'projects/projects.html', currentStatus)
