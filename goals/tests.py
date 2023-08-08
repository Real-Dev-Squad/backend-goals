from rest_framework.test import APITestCase, APIClient
from .models import Goal
from .fixtures import goals as goals_data


class GoalsTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = APIClient()

        for goal in goals_data:
            Goal.objects.create(**goal["fields"])

        super(GoalsTest, cls).setUpClass()

    def test_get_goals(self):
        _response = self.client.get('/goal/')
        _response_data = _response.json()

        _response_goals_data = _response_data["data"]
        _response_goal_data = _response_goals_data[0]["attributes"]

        assert _response.status_code == 200
        assert len(_response_goals_data) > 0
        assert "title" in _response_goal_data
        assert "description" in _response_goal_data
        assert "assigned_by" in _response_goal_data
        assert "status" in _response_goal_data

    def test_get_goals_filtered(self):
        goal_title = goals_data[2]["fields"]["title"]
        _response = self.client.get(f'/goal/?title={goal_title}')
        _response_data = _response.json()

        _response_goals_data = _response_data["data"]
        _response_goal_data = _response_goals_data[0]["attributes"]

        assert _response.status_code == 200
        assert len(_response_goals_data) > 0
        assert "title" in _response_goal_data
        assert goal_title == _response_goal_data["title"]
        assert "description" in _response_goal_data
        assert "assigned_by" in _response_goal_data
        assert "status" in _response_goal_data
