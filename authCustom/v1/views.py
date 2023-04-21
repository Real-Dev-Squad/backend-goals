from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authCustom.models import Token_Custom
from authCustom.v1.serializer import TokenSerializer
from base.utils import env

class GoalAuthTokenViewSet(ModelViewSet):
    serializer_class = TokenSerializer
    http_method_names = ['post']
    
    def get_queryset(self):
        return []

    def create(self, request, *args, **kwargs):
        try:
            user_id = request.data.get('user_id', None)
            rest_key = request.data.get('rest_key', "")
            if rest_key != env('REST_KEY'):
                raise Exception("Wrong REST_KEY")
            elif user_id is None:
                raise Exception("Provide A User Id")


            try:
                token = Token_Custom.objects.get(user_id=user_id)
                if token.is_invalid():
                    token = token.update_token()

            except Token_Custom.DoesNotExist:
                token = Token_Custom.objects.create(user_id=user_id)

            token_data = TokenSerializer(token).data
            return Response({"message": "Goal site token generated succesfully", "token": token_data})
        except Exception as e:
            return Response(e.args[0], status=400, exception=True)
    