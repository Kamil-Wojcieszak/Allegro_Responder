import requests
import json


CONFIG = dict()


def get_authorization_code():
	authorization_redirect_url = CONFIG['auth_url'] + '?response_type=code&client_id=' + CONFIG['client_id'] + '&redirect_uri=' + CONFIG['redirect_uri']
	print("Zaloguj do Allegro: ")
	print("---  " + authorization_redirect_url + "  ---")
	authorization_code = input('code: ')
	return authorization_code


def get_refresh_token(authorization_code):
	try:
		data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': CONFIG['redirect_uri']}
		access_token_response = requests.post(CONFIG['token_url'], data=data, verify=False, allow_redirects=False, auth=(CONFIG['client_id'], CONFIG['client_secret']))
		tokens = json.loads(access_token_response.text)
		return tokens
	except requests.exceptions.HTTPError as err:
		raise SystemExit(err)


class Loging:
	refresh_token = None
	access_token = None

	def get_new_token_pair(self):
		if self.refresh_token is None:
			x = get_refresh_token(get_authorization_code())
			self.access_token = x['access_token']
			self.refresh_token = x['refresh_token']
			return
		try:
			data = {'grant_type': 'refresh_token', 'refresh_token': self.refresh_token, 'redirect_uri': CONFIG['redirect_uri']}
			access_token_response = requests.post(CONFIG['token_url'], data=data, verify=False, allow_redirects=False, auth=(CONFIG['client_id'], CONFIG['client_secret']))
			tokens = json.loads(access_token_response.text)
			self.access_token = tokens['access_token']
			self.refresh_token = tokens['refresh_token']
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)

	def __init__(self, enviorment):
		try:
			with open('config.json') as f:
				data = json.load(f)
				global CONFIG
				CONFIG = data[enviorment]
		except FileNotFoundError:
			print("File not found")
			exit(-1)



