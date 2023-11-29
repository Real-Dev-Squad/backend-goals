import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.conf import LazySettings

from apps.conftest import get_user_token
from apps.base.constants import SUPER_USER_ROLE

settings = LazySettings()


@pytest.mark.django_db
class TestUsersViewSet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()

    @classmethod
    def set_user_token(self, user):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=get_user_token(user))

    def test_create_or_get_user(self, client):
        rds_id = "test1"
        user_data = {
            "data": {
                "type": "User",
                "attributes": {
                    "rds_id": rds_id,
                    "roles": {
                        "member": True
                    }
                }
            }
        }
        self.client.credentials(HTTP_REST_KEY=settings.RDS_BACKEND_SECRET_KEY)

        _response = self.client.post(
            "/api/v1/user/", user_data,  format="vnd.api+json")
        assert _response.status_code == status.HTTP_201_CREATED
        _response_data = _response.json()

        _response_data = _response_data["data"]
        user_data = {"id": _response_data["id"],
                     **_response_data["attributes"]}

        assert user_data["rds_id"] == rds_id
        assert "token" in user_data
        assert "roles" in user_data
        assert user_data["roles"]["member"] == True

    def test_get_user(self, client, user_t1):
        self.client.credentials(HTTP_AUTHORIZATION=get_user_token(user_t1))

        _response = self.client.get(
            f"/api/v1/user/{str(user_t1.id)}/",  format="vnd.api+json")
        assert _response.status_code == status.HTTP_200_OK
        _response_data = _response.json()

        _response_data = _response_data["data"]
        user_data = {"id": _response_data["id"],
                     **_response_data["attributes"]}

        assert user_data["rds_id"] == user_t1.rds_id

    def test_list_users(self, client, user_t1, user_t2):
        self.client.credentials(HTTP_AUTHORIZATION=get_user_token(user_t1))

        _response = self.client.get(
            f"/api/v1/user/",  format="vnd.api+json")

        assert _response.status_code == status.HTTP_403_FORBIDDEN

        # giving a role to authorize
        user_t1.roles[SUPER_USER_ROLE] = True
        user_t1.save()

        _response = self.client.get(
            f"/api/v1/user/",  format="vnd.api+json")

        assert _response.status_code == status.HTTP_200_OK
