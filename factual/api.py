"""
Factual API driver
"""

import requests
import json
from oauth_hook import OAuthHook

API_V3_HOST        = "http://api.v3.factual.com"
DRIVER_VERSION_TAG = "factual-python-driver-1.0"

class Factual(object):
    def __init__(self, key, secret):
      self.key = key
      self.secret = secret
      self.api = self.API(self._generate_token(key, secret))

    def table(self, table):
        pass

    def crosswalk(self, factual_id):
        pass

    def resolve(self, values):
        pass

    def _generate_token(self, key, secret):
        access_token = OAuthHook(consumer_key = key, consumer_secret = secret, header_auth=True)
        return access_token


    class API(object):
        def __init__(self, access_token):
            self.access_token = access_token

        def execute(self, query):
            # TODO - action, path, and params should be included in query
            action = 'read'
            path = 't/places'
            params = { 'search':"sushi santa monica"}
        
            request = self._handle_request(action, path, params)
            return request
            
        # TODO - return schema
        def schema(query):
            pass    

        def _handle_request(self, action, path, params):
            request = self._make_request(path, params)
            payload = json.loads(request)
            # TODO - Raise Error if payload['status'] != 'ok'
            return payload["response"]
            
        def _make_request(self, path, params):
            url = API_V3_HOST + "/" + path + "?" + self._make_query_string(params)
            headers = { "X-Factual-Lib" : DRIVER_VERSION_TAG }
            return requests.get(url, headers=headers, hooks={'pre_request': self.access_token}).text

        def _make_query_string(self, params):
            # TODO - Convert params dict to str
            query_string = "q=sushi+santa+monica&limit=1"
            return query_string 
