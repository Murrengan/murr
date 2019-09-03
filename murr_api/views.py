from rest_framework import generics
from Murren.models import Murren
from .serializers import MurrenSerializer


class MurrenList(generics.ListAPIView):
    queryset = Murren.objects.all()
    serializer_class = MurrenSerializer


class MurrenById(generics.RetrieveAPIView):

    queryset = Murren.objects.all()
    serializer_class = MurrenSerializer
