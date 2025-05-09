import requests

class ValorantAPI:
    def __init__(
            self, 
            api_key: str,
            version = 'v1'
        ):
        self.version = version
        self.base_uri = f"https://api.henrikdev.xyz/valorant/{self.version}"
        self.header = {
            "Authorization": api_key
        }

    def get_account(
            self, 
            name: str, 
            tag: str
        ):
        uri = f"{self.base_uri}/account/{name}/{tag}"
        response = requests.get(
            url = uri, 
            headers = self.header
        )
        response.raise_for_status()
        return response.json()

    def get_mmr(
            self, 
            region: str, 
            name: str, 
            tag: str
        ):
        if self.version == 'v1':
            raise ValueError('Cannot Use get_mmr() in API v1. You need to use more higher version than v2.')

        else:
            uri = f"{self.base_uri}/mmr/{region}/{name}/{tag}"
            response = requests.get(
                url = uri, 
                headers = self.header
            )
            response.raise_for_status()
            return response.json()