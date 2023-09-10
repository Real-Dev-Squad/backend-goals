import pytest

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


def get_user_token(user):
    return f'Bearer {str(RefreshToken.for_user(user).access_token)}'


@pytest.fixture
def new_user_factory(db):
    def create_app_user(rds_id):
        user = User.objects.create_user(rds_id=rds_id)
        return user

    yield create_app_user


@pytest.fixture
def user_t1(db, new_user_factory):
    user = new_user_factory("hello_1")
    return user


@pytest.fixture
def user_t2(db, new_user_factory):
    return new_user_factory("hello_2")
