from httpx import get
from .errors import InstanceError
from .schema import HeartbeatResponse, AppInfo, Distribution, KunyakinResponse

class LunaInstance:
    api_base_url: str
    def __init__(self, api_base_url: str="https://api.lunastore.app"):
        self.api_base_url = f"{api_base_url}/method"
    def heartbeat(self) -> HeartbeatResponse:
        METHOD_URL = f"{self.api_base_url}/service/heartbeat/"
        response = get(METHOD_URL)
        if response.status_code != 200:
            raise InstanceError(f"Instance api returned status code {response.status_code} on url {METHOD_URL}, content: {response.text}")
        return response.json()
    
    def get_app_info(self, app_id: int) -> AppInfo:
        METHOD_URL = f"{self.api_base_url}/marketplace/getAppInfo/"
        response = get(METHOD_URL, params={"id": app_id})
        if response.status_code != 200:
            raise InstanceError(f"Instance api returned status code {response.status_code} on url {METHOD_URL}, content: {response.text}")
        return response.json()
    
    def search(self, query: int) -> list[AppInfo]:
        METHOD_URL = f"{self.api_base_url}/marketplace/search/"
        response = get(METHOD_URL, params={"query": query})
        if response.status_code != 200:
            raise InstanceError(f"Instance api returned status code {response.status_code} on url {METHOD_URL}, content: {response.text}")
        # process response. Lunastore api returns list in strange format, so we have to convert it
        resp = response.json()
        o: list[AppInfo] = []
        for idx in resp:
            o.append(resp[idx])
        return o

    def get_app_list(self, category_id: int) -> list[AppInfo]:
        METHOD_URL = f"{self.api_base_url}/category/getAppList/"
        response = get(METHOD_URL, params={"id": category_id})
        if response.status_code != 200:
            raise InstanceError(f"Instance api returned status code {response.status_code} on url {METHOD_URL}, content: {response.text}")
        # process response. Lunastore api returns list in strange format, so we have to convert it
        resp = response.json()
        o: list[AppInfo] = []
        for idx in resp:
            o.append(resp[idx])
        return o

    def get_dist_list(self, app_id: int) -> list[Distribution]:
        METHOD_URL = f"{self.api_base_url}/distribution/getDistributionsList/"
        response = get(METHOD_URL, params={"id": app_id})
        if response.status_code != 200:
            raise InstanceError(f"Instance api returned status code {response.status_code} on url {METHOD_URL}, content: {response.text}")
        # process response. Lunastore api returns list in strange format, so we have to convert it
        resp = response.json()
        o: list[Distribution] = []
        for idx in resp:
            o.append(resp[idx])
        return o
    
    def kunyakin(self) -> KunyakinResponse:
        METHOD_URL = f"{self.api_base_url}/service/kunyakin/"
        response = get(METHOD_URL)
        if response.status_code != 200:
            raise InstanceError(f"Instance api returned status code {response.status_code} on url {METHOD_URL}, content: {response.text}")
        return response.json()