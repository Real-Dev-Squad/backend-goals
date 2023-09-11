# from rest_framework.decorators import api_view, parser_classes
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
# from django.utils import timezone

# from .models import User
# from .utils import env


# @api_view(["POST"])
# @parser_classes([JSONParser])
# def goal_auth_token(request, userId):
#     try:
#         RDS_BACKEND_SECRET_KEY = request.data.get('RDS_BACKEND_SECRET_KEY')
#         if RDS_BACKEND_SECRET_KEY != env('RDS_BACKEND_SECRET_KEY'):
#             raise Exception("Wrong RDS_BACKEND_SECRET_KEY")

#         try:
#             token = User.objects.get(userId=userId)
#             if token.is_invalid(createdTime=token.created.timestamp()):
#                 User.objects.filter(userId=userId).update(
#                     auth_token=User.generate_key(), created=timezone.now())
#                 token = User.objects.get(userId=userId)
#         except User.DoesNotExist:
#             token = User(userId=userId)
#             token.save()

#         return Response({"message": "Goal site token generated succesfully", "token": token.auth_token})
#     except Exception as e:
#         return Response(e.args[0], status=400, exception=True)
