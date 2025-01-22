import requests

class ApiKeyManagerClient:
    def __init__(self, api_url: str, api_reference_id: str, api_key_id: str, api_key: str):
        self.api_url = api_url
        response = requests.get(self.api_url)
        print(response)
        self.api_reference_id = api_reference_id
        self.api_key_id = api_key_id
        self.api_key = api_key
    
    def verify_api_key(self):
        response = requests.post(self.api_url, 
                                 {
                                    "api_reference_id":  self.api_reference_id,
                                    "api_key_id": self.api_key_id,
                                    "api_key": self.api_key
                                 }
                                )
        print(response)
    
    