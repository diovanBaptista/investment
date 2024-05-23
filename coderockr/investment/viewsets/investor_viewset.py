from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Investor
from ..serializers import InvestorSerializer


class InvestorViewSet(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]