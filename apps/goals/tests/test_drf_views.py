import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.conf import LazySettings

from apps.conftest import get_user_token
from apps.goals.fixtures import goals
from apps.goals.models import Goal

settings = LazySettings()


@pytest.mark.django_db
class TestGoalsViewSet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        for goal in goals:
            Goal.objects.create(**goal["fields"])

    def test_get_goals(self, user_t1):
        self.client.credentials(HTTP_AUTHORIZATION=get_user_token(user_t1))
        _response = self.client.get('/api/v1/goal/', format="vnd.api+json")
        _response_data = _response.json()

        _response_goals_data = _response_data["data"]
        _response_goal_data = _response_goals_data[0]["attributes"]

        assert _response.status_code == status.HTTP_200_OK
        assert len(_response_goals_data) > 0
        assert "title" in _response_goal_data
        assert "description" in _response_goal_data
        assert "assigned_by" in _response_goal_data
        assert "status" in _response_goal_data

    def test_get_goals_filtered(self, user_t1):
        goal_title = goals[1]["fields"]["title"]
        self.client.credentials(HTTP_AUTHORIZATION=get_user_token(user_t1))
        _response = self.client.get(f'/api/v1/goal/?title={goal_title}', format="vnd.api+json")
        _response_data = _response.json()

        _response_goals_data = _response_data["data"]
        _response_goal_data = _response_goals_data[0]["attributes"]

        assert _response.status_code == status.HTTP_200_OK
        assert len(_response_goals_data) > 0
        assert "title" in _response_goal_data
        assert goal_title == _response_goal_data["title"]
        assert "description" in _response_goal_data
        assert "assigned_by" in _response_goal_data
        assert "status" in _response_goal_data
