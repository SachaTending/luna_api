from httpx import get
from .errors import InstanceError

class LunaInstance:
    api_base_url: str
    def __init__(self, api_base_url: str="https://api.lunastore.app"):
        self.api_base_url = f"{api_base_url}/method"
    def heartbeat(self):
        METHOD_URL = f"{self.api_base_url}/service/heartbeat/"
        response = get(METHOD_URL)
        if response.status_code != 200:
            raise InstanceError(f"Instance api returned status code {response.status_code} on url {METHOD_URL}, content: {response.text}")
        return response.json()
    
    def get_app_info(self, app_id: int):
        METHOD_URL = f"{self.api_base_url}/marketplace/getAppInfo/"
        response = get(METHOD_URL, params={"id": app_id})
        if response.status_code != 200:
            raise InstanceError(f"Instance api returned status code {response.status_code} on url {METHOD_URL}, content: {response.text}")
        return response.json()
    
    def search(self, query: int):
        METHOD_URL = f"{self.api_base_url}/marketplace/search/"
        response = get(METHOD_URL, params={"query": query})
        if response.status_code != 200:
            raise InstanceError(f"Instance api returned status code {response.status_code} on url {METHOD_URL}, content: {response.text}")
        return response.json()
    
    def get_app_list(self, category_id: int):
        METHOD_URL = f"{self.api_base_url}/category/getAppList/"
        response = get(METHOD_URL, params={"id": category_id})
        if response.status_code != 200:
            raise InstanceError(f"Instance api returned status code {response.status_code} on url {METHOD_URL}, content: {response.text}")
        return response.json()

    def get_dist_list(self, app_id: int):
        METHOD_URL = f"{self.api_base_url}/distribution/getDistributionsList/"
        response = get(METHOD_URL, params={"id": app_id})
        if response.status_code != 200:
            raise InstanceError(f"Instance api returned status code {response.status_code} on url {METHOD_URL}, content: {response.text}")
        return response.json()
    
    def kunyakin(self):
        METHOD_URL = f"{self.api_base_url}/service/kunyakin/"
        response = get(METHOD_URL)
        if response.status_code != 200:
            raise InstanceError(f"Instance api returned status code {response.status_code} on url {METHOD_URL}, content: {response.text}")
        return response.json()