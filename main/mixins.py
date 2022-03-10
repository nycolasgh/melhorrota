from django.conf import settings
import requests
import json


'''
Handles directions from Google
'''


def Directions(*args, **kwargs):

	result = requests.get(
		'https://maps.googleapis.com/maps/api/directions/json?',
		 params={
		 'origin': origin,  # cria waypoints aqui e optimization true tbm
		 'destination': destination,
         'waypoints': waypoints,
		 'optimization': True,
		 "key": settings.GOOGLE_API_KEY,
		 })

	directions = result.json()

	if directions["status"] == "OK":

		route = directions["routes"][0]["legs"][0]
		origin = route["start_address"]
		destination = route["end_address"]
		distance = route["distance"]["text"]
		duration = route["duration"]["text"]


	return {
		"origin": origin,
		"destination": destination,
		"distance": f'{distance} Km',
		"duration": f'{duration} min.',
		}