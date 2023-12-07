from sqlite3 import InternalError
from openai_plus.chat_gpt.language_translator import translate_query
from openai_plus.serializers.chat_query import ChatQuerySerializer
from openai_plus.models import ChatQuery
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class QueryViewSet(APIView):

    def get(self, request, value):
        if value == "2":
            raise InternalError("server issue")
        if value == "5":
            raise NotImplementedError("server issue")
        if value == "4":
            return Response(data={"message": "please provide query"}, status=500)
        if value == "6":
            return Response(data={"message": "please provide query"}, status=status.HTTP_501_NOT_IMPLEMENTED)
        if value == "3":
            return Response(data={"message": "please provide query"}, status=400)
        queryset = ChatQuery.objects.all()
        ser = ChatQuerySerializer(queryset, many=True)
        print(ser.data)
        return Response(data=ser.data, status=200)

    def post(self, request):
        data = request.data.copy()
        query = data.get("query", None)
        language = data.get("language", None)
        if not query:
            return Response(data={"message": "please provide query"}, status=400)
        if not language:
            return Response(data={"message": "please provide language"}, status=400)
        try:
            data['result'] = translate_query(query, language)
        except Exception as e:
            print(e)
            return Response(data={"message": f"Cant not translate the query into {language}"}, status=400)
        ser = ChatQuerySerializer(data=data)
        if ser.is_valid():
            ser.save()
        return Response(data=data, status=200)

    