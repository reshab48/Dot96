from django.conf import settings
import requests

def check_recaptcha_ajax(response):
	data = {
		'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		'response' : response,
	}
	r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
	result = r.json()
	if result['success']:
		return True
	else:
		return False