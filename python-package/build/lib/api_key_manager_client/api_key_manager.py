import requests

class ApiKeyManagerClient:
    def __init__(self, api_url: str, version: str = 'v1'):    
        self.api_url = api_url    
        self.version = version
    
    def verify_api_key(self, api_reference_id: str, api_key_id: str, api_key: str):
        response = requests.post(f'{self.api_url}/api/{self.version}/api-key-manager/verify-key', 
                                 json={
                                    "api_reference_id": api_reference_id,
                                    "api_key_id": api_key_id,
                                    "api_key": api_key
                                 }
                                )
        print(response.json())
    
    