import requests

import errors

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
        """Get your Valorant Account from API.

        Fetch your Valorant Account details data from Henrik's API.

        :param str api_key: API Key
        :param str name: Account Name (display name before #.)
        :param str tag: Account Tagline (display name after #.)
        :return: Returns your Valorant account data fetched from Henrik API.
        :rtype: dict
"""
        uri = f"{self.base_uri}/account/{name}/{tag}"
        response = requests.get(
            url = uri, 
            headers = self.header
        )
        response.raise_for_status()
        if response.status_code == 404:
            raise errors.AccountNotFound('Account not found.')
        return response.json()

    def get_account_puuid(
            self, 
            puuid: str
        ):
        """Get your Valorant Account by puuid from API.

        Fetch your Valorant Account details data by puuid from Henrik's API.

        :param str api_key: API Key
        :param str puuid: Account puuid (e.g. 6955434b-6ab7-5cc2-993a-73072fb585c4)
        :return: Returns your Valorant account data fetched from Henrik API.
        :rtype: dict
"""
        uri = f"{self.base_uri}/by-puuid/account/{puuid}"
        response = requests.get(
            url = uri, 
            headers = self.header
        )
        response.raise_for_status()
        if response.status_code == 404:
            raise errors.AccountNotFound('Account not found.')
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