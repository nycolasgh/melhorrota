from django.shortcuts import render
from django.conf import settings
from .mixins import Directions

'''
Basic view for routing 
'''
def route(request):


	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, 'main/route.html', context)

