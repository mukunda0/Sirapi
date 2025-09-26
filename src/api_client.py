import requests

BASE_URL = "https://api.restful-api.dev/objects"

"""class APIClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def patch_object(self, object_id: str, data: dict):
        #PATCH an object by ID
        url = f"{self.base_url}/{object_id}"
        response = requests.patch(url, json=data)
        return response"""
class APIClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def create_object(self, data: dict):
        """Create a new object (POST)"""
        response = requests.post(self.base_url, json=data)
        return response

    def patch_object(self, object_id: str, data: dict):
        """PATCH an object by ID"""
        url = f"{self.base_url}/{object_id}"
        response = requests.patch(url, json=data)
        return response
