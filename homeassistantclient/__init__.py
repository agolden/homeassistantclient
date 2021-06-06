import requests
import json

class HAAPI(object):
	def __init__(
		self,
		host,
		access_token,
		is_secure=False,
	):
		self.host = host
		self.access_token = access_token
		self.is_secure = is_secure

	def __base_url(self):
		return ("https" if self.is_secure else "http") + "://" + self.host + "/api"

	def __base_headers(self):
		api_key = "Bearer " + self.access_token
		return {"Authorization": api_key }

	def get_state(self, entity_id):
		url = self.__base_url() + "/states/" + entity_id
		return requests.get(url, headers=self.__base_headers()).json()