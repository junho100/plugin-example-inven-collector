import json
import logging
from spaceone.core.connector import BaseConnector
import requests

_LOGGER = logging.getLogger("cloudforet")


class ResourceConnector(BaseConnector):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def list_servers(token, tenantId) -> dict:
        response = requests.get(f"https://kr1-api-instance-infrastructure.nhncloudservice.com/v2/{tenantId}/servers", headers={
            "Content-Type": "application/json",
            "X-Auth-Token": token
        })
        return response.json()

    def get_token(self, secret_data):
        response = requests.post("https://api-identity-infrastructure.nhncloudservice.com/v2.0/tokens", json={
            "auth": {
                "tenantId": secret_data["tenant_id"],
                "passwordCredentials": {
                    "username": secret_data["client_id"],
                    "password": secret_data["client_secret"]
                }
            }
        }, headers={"Content-Type": "application/json"})

        if response.status_code == 200:
            return response.json()["access"]["token"]["id"], secret_data["tenant_id"]
        else:
            raise Exception(f"Failed to get token. {response.json()}")
