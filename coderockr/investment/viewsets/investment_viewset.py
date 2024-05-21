from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Investiment
from ..serializers import InvestimentSerializer


class InvestimentationViewSet(viewsets.ModelViewSet):
    queryset = Investiment.objects.all()
    serializer_class = InvestimentSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]
