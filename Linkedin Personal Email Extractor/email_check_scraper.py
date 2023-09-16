import requests

def email_checker(email):
	url = "https://email-social-media-checker.p.rapidapi.com/check_email"

	querystring = {"email":f"{email}"}

	headers = {
		"X-RapidAPI-Key": "8da795aa71msh3cee0f5a50328e0p10aa59jsne899580ef625",
		"X-RapidAPI-Host": "email-social-media-checker.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	# print(response.json())
	return response.json()