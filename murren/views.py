# 3rd party
from rest_framework.response import Response
from rest_framework.views import APIView


class MurrensMethods(APIView):

    def get(self, request):
        data = {'Who is Murren?': 'Murren is a main part of Murrengan'}
        return Response(data)
