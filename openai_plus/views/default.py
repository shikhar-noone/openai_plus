from openai_plus.chat_gpt.language_translator import translate_query
from openai_plus.serializers.chat_query import ChatQuerySerializer
from openai_plus.models import ChatQuery
from rest_framework.views import APIView
from rest_framework.response import Response

class DefaultViewSet(APIView):

    def get(self, request):
        try:
            print("In default")
            queryset = ChatQuery.objects.all()
            ser = ChatQuerySerializer(queryset, many=True)
            return Response(data=ser.data, status=200)
        except Exception as err:
            return Response(data={"message":"default view"})


    