from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from .authentications import TokenCustomAuthentication
from .views import goal_auth_token
from .utils import env
from .models import Token_Custom

# DEMO API to test authentication


@api_view()
@authentication_classes([TokenCustomAuthentication])
@permission_classes([IsAuthenticated])
def Authenticated(request):
    return Response("Hello World", status=200)


def get_previous_month_date(date):
    month = date.month
    month -= 1
    year = date.year
    day = date.day - 1
    if month <= 0:
        month = 12
        year -= 1
    return timezone.datetime(day=day, year=year, month=month, hour=date.hour, tzinfo=date.astimezone().tzinfo)


class AuthenticateTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = APIRequestFactory()
        token = Token_Custom(userId="Vinayak")
        token.save()
        cls.token = token
        super(AuthenticateTest, cls).setUpClass()

    def test_auth_without_cookie(self):
        _request = self.factory.post('authToken/auth')
        _response = Authenticated(_request)
        self.assertEqual(_response.data[0]["detail"].title(
        ), "Authentication Credentials Were Not Provided.")
        self.assertEqual(_response.status_code, 403)

    def test_auth_with_wrong_cookie(self):
        _request = self.factory.get('authToken/auth')
        _request.COOKIES['goal-site-session'] = self.token.auth_token + "1"
        _response = Authenticated(_request)
        self.assertEqual(
            _response.data[0]["detail"].title(), "Token Is Expired Or Invalid")
        self.assertEqual(_response.status_code, 403)

    def test_auth_with_expired_cookie(self):
        _request = self.factory.get('authToken/auth')
        time = timezone.now()
        time = get_previous_month_date(time)
        Token_Custom.objects.filter(
            userId=self.token.userId).update(created=time)
        _request.COOKIES['goal-site-session'] = self.token.auth_token
        _response = Authenticated(_request)
        self.assertEqual(
            _response.data[0]["detail"].title(), "Token Is Expired Or Invalid")
        self.assertEqual(_response.status_code, 403)

    def test_auth_with_cookie(self):
        _request = self.factory.get('authToken/auth')
        _request.COOKIES['goal-site-session'] = self.token.auth_token
        _response = Authenticated(_request)
        self.assertEqual(_response.data, "Hello World")
        self.assertEqual(_response.status_code, 200)


class Get_Auth_token_Test(APITestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = APIRequestFactory()
        super(Get_Auth_token_Test, cls).setUpClass()

    def test_get_auth_token_without_restkey(self):
        _request = self.factory.post('authToken//get_token')
        _response = goal_auth_token(_request, userId="vinayak")
        self.assertEqual(_response.data, 'Wrong REST_KEY')

    def test_get_auth_token_with_restkey(self):
        _request = self.factory.post(
            'authToken//get_token', {"rest_key": env("REST_KEY")}, format="json")
        _response = goal_auth_token(_request, userId="vinayak")

        self.assertEqual(_response.data["message"],
                         'Goal site token generated succesfully')
        self.assertEqual(_response.status_code, 200)
        self.assertIn("token", _response.data)
        self.assertIs(type(_response.data["token"]), str)
