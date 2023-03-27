from rest_framework.test import APITestCase, APIRequestFactory
from .models import Goal, UserGoal
from .fixtures import goals as goals_data, usergoals as usergoals_data
from .views import GoalViewSet, UserGoalViewSet


class GoalsTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = APIRequestFactory()
        for goal in goals_data:
            Goal.objects.create(**goal["fields"])

        for user_goal in usergoals_data:
            goal = Goal.objects.get(pk=user_goal["fields"]["goal"])
            user_goal["fields"]["goal"] = goal
            UserGoal.objects.create(**user_goal["fields"])
        super(GoalsTest, cls).setUpClass()

    def test_get_goals(self):
        _response = self.factory.get("/goal")
        _response = GoalViewSet.as_view({'get': 'list'})(_response)

        for goal_index in range(len(goals_data)):
            for goal_attribute in goals_data[goal_index]["fields"].keys():
                if goal_attribute == "createdAt":
                    continue
                self.assertEqual(
                    _response.data[goal_index][goal_attribute], goals_data[goal_index]["fields"][goal_attribute])

    def test_get_usergoals(self):
        _response = self.factory.get("/usergoal")
        _response = UserGoalViewSet.as_view({'get': 'list'})(_response)

        for usergoal_index in range(len(usergoals_data)):
            for usergoal_attribute in usergoals_data[usergoal_index]["fields"].keys():
                if usergoal_attribute == "startsOn" or usergoal_attribute == "endsOn":
                    continue
                elif usergoal_attribute == "goal":
                    goal_id = usergoals_data[usergoal_index]["fields"][usergoal_attribute].id
                    self.assertEqual(_response.data[usergoal_index][usergoal_attribute]["id"], str(goal_id))
                else:
                    self.assertEqual(
                        _response.data[usergoal_index][usergoal_attribute], usergoals_data[usergoal_index]["fields"][usergoal_attribute])
