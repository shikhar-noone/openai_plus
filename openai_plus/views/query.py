from sqlite3 import InternalError
from openai_plus.chat_gpt.language_translator import translate_query
from openai_plus.serializers.chat_query import ChatQuerySerializer
from openai_plus.models import ChatQuery
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from logging import getLogger

logger = getLogger('custom_logger')
class QueryViewSet(APIView):

    def get(self, request, value):
        logger.debug("this log should go console.")
        logger.info("this log should go in testfile.log as well as in console.")
        logger.warning("this log should go in testfile.log and testlogfile.log as well as in console.")
        if value == "ir":
            raise InternalError("server issue")
        if value == "test-success":
            return Response(data={"message": "yes boi"}, status=400)
        if value == "test-html":
            res = """
                <html>
                <head>
                    <script>
                        const turn = (value) => {
                            console.log(value, 'where');
                            document.getElementById('demo').innerHTML = 'Hello World';
                            if (value === 'red') {
                                document.getElementById('demo').style.color = 'red';
                            } else {
                                document.getElementById('demo').style.color = 'blue';
                            }
                        }
                    </script>
                </head>
                <body>
                    <h1 id='demo'>Hey bro, what's up!! heheehee, how did I do that, No, watch metf joinjh hshs no man</h1>
                    <h1 id='demo'>should i do anything else</h1>
                    <button onclick="turn('red')">Click me</button>
                </body>
                </html>
            """
            return HttpResponse(res, content_type="text/HTML")
        if value == "sockets":
            res = """
                <html>
                <head>
                    <script>
                    </script>
                </head>
                <body>
                    <h1 id='IP'>IP(Internet protocol) is a way of delivering message from client to host by dividing the message in small packets and binding them source and destination IP address and sequence number which is then routed via several routers. routers use IP address to figure out correct path to forward the packets and finally the packets are assembled at destination</h1>
                    <h1 id='TCP'>TCP is a protocol which basically handles how transmission is controled. it first creates a connection via 3 way handshake, then messages or packets are sent. It is a reliable connection, health check of connection is also done after a period to make the connection reliable, incase a packet does not ends up at destination, TCP can handle the situation. But the maintainence of the connection results in latency.</h1>
                    <h1 id='http'>In case of Http request, the protocol is set for communication between client and host, the format is also set. each request is stateless and independent of previous reequest. persistent TCP connection can be maintained here using Connection: keep-alive header available in HTTP:V1.1 but both client and host have to communicate on same protocol. Nothing can be pushed without a proper response.</h1>
                    <h1 id='socket'>In case of sockets, there is a connection maintained between host and client. which can be maintained for long period as well as for short period of time. the message format and communication protocol is not fixed here. It can be maintained if client and host wants to maintain it. After successful connection, one sided messages can be passed.</h1>
                </body>
                </html>
            """
        if value == "graphs":
            res = """
                <html>
                <head>
                    <script>
                    </script>
                </head>
                <body>
                    <h1 id='dijkstra'>Dijkstra AND bellman ford are algorithms to find out minimum distance between two nodes, in dijkstra, it assumes that all edges weights are positive and takes a greedy approach by sorting edges on the basis of weights.
                    In both algos, basically starting from a node(start_node) we loop through all edges and maintain a map of smallest distance from root node, if weight of this edge + smallest distance to reach to start_node from mapper is less than the smallest distance present in mapper, then we update it. else if it greater than we pop it</h1>
                    <h1 id='TCP'>TCP is a protocol which basically handles how transmission is controled. it first creates a connection via 3 way handshake, then messages or packets are sent. It is a reliable connection, health check of connection is also done after a period to make the connection reliable, incase a packet does not ends up at destination, TCP can handle the situation. But the maintainence of the connection results in latency.</h1>
                    <h1 id='http'>In case of Http request, the protocol is set for communication between client and host, the format is also set. each request is stateless and independent of previous reequest. persistent TCP connection can be maintained here using Connection: keep-alive header available in HTTP:V1.1 but both client and host have to communicate on same protocol. Nothing can be pushed without a proper response.</h1>
                    <h1 id='socket'>In case of sockets, there is a connection maintained between host and client. which can be maintained for long period as well as for short period of time. the message format and communication protocol is not fixed here. It can be maintained if client and host wants to maintain it. After successful connection, one sided messages can be passed.</h1>
                </body>
                </html>
            """
            return HttpResponse(res, content_type="text/HTML")
        if value == "all":
            queryset = ChatQuery.objects.all()
            ser = ChatQuerySerializer(queryset, many=True)
            print(ser.data)
            return Response(data=ser.data, status=200)
        return HttpResponse('<H1>Not found.</H1>', content_type="text/HTML")

    def post(self, request):
        print("I was here")
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

    