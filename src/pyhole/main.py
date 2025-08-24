from restpylot import RestClient

from .classes.local_dns import Config

class PiHole(RestClient):
    def __init__(self, base_url, password, debug=False):
        """
        Initialize the PiHole class.

        :param base_url: The base URL for the Pi-hole API.
        :param api_token: The API token for authentication.
        :param debug: Enable debug mode if True.
        """
        self.base_url = base_url
        self.password = password
        
        super().__init__(base_url, debug=debug)
        
        self.auth_obj = self._auth()
        super().__init__(base_url, api_key=self.auth_obj['session']['sid'], api_key_type='sid', debug=debug)
        
    def _auth(self):
        endpoint = '/auth'
        payload = dict(
            password = self.password
        )
        return self.post(endpoint, json=payload)

    def close_session(self):
        self.delete('/auth')
        return self.close()

    def Config(self):
        return Config(self)