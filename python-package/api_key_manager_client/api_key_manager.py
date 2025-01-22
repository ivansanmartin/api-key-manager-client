import requests

class ApiKeyManagerClient:
    def __init__(self, api_url: str, version: str = 'v1'):    
        self.api_url = api_url    
        self.version = version
    
    def verify_api_key(self, api_reference_id: str, api_key_id: str, api_key: str):
        try:
            response = requests.post(
                f'{self.api_url}/api/{self.version}/api-key-manager/verify-key',
                json={
                    "api_reference_id": api_reference_id,
                    "api_key_id": api_key_id,
                    "api_key": api_key
                }
            )
            
            response.raise_for_status()

            data = response.json()

            return data

        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except requests.exceptions.TooManyRedirects as redirect_err:
            print(f"Too many redirects occurred: {redirect_err}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        return None
            
    
    