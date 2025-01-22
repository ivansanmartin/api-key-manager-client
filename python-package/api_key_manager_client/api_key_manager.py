import requests

class ApiKeyManagerClient:
    def __init__(self, api_url: str):    
        self.api_url = api_url    
    
    def verify_api_key(self, api_reference_id: str, api_key_id: str, api_key: str):
        response = requests.post(self.api_url, 
                                 {
                                    "api_reference_id": api_reference_id,
                                    "api_key_id": api_key_id,
                                    "api_key": api_key
                                 }
                                )
        print(response.json())
    
    