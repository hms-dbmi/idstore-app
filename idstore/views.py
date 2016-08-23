from rest_framework import viewsets
from .serializers import IdPairSerializer
from .models import IdPair
from rest_framework import generics


class IdPairViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = IdPair.objects.all()
    serializer_class = IdPairSerializer


class IdPairCreateViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows the ID Mapping to be created or retrieved.
    """
    serializer_class = IdPairSerializer

    def get_queryset(self):

        udn_id = self.request.query_params.get('udn_id', None)

        if udn_id is not None:
            queryset = IdPair.objects.get_or_create(udn_id=udn_id)
        else:
            return None
        return queryset

