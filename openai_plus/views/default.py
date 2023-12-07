from openai_plus.chat_gpt.language_translator import translate_query
from openai_plus.serializers.chat_query import ChatQuerySerializer
from openai_plus.models import ChatQuery
from rest_framework.views import APIView
from rest_framework.response import Response

class DefaultViewSet(APIView):

    def get(self, request):
        queryset = ChatQuery.objects.all()
        ser = ChatQuerySerializer(queryset, many=True)
        print(ser.data)
        return Response(data=ser.data, status=200)


    