import requests


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint: str):
        return requests.get(f"{self.base_url}/{endpoint.lstrip('/')}")

    def post(self, endpoint: str, data=None):
        return requests.post(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            json=data
        )