from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.utils import timezone

from .models import User
from .utils import env


@api_view(["POST"])
@parser_classes([JSONParser])
def goal_auth_token(request, userId):
    try:
        rest_key = request.data.get('rest_key')
        if rest_key != env('REST_KEY'):
            raise Exception("Wrong REST_KEY")

        try:
            token = User.objects.get(userId=userId)
            if token.is_invalid(createdTime=token.created.timestamp()):
                User.objects.filter(userId=userId).update(
                    auth_token=User.generate_key(), created=timezone.now())
                token = User.objects.get(userId=userId)
        except User.DoesNotExist:
            token = User(userId=userId)
            token.save()

        return Response({"message": "Goal site token generated succesfully", "token": token.auth_token})
    except Exception as e:
        return Response(e.args[0], status=400, exception=True)
