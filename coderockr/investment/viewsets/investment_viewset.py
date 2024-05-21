from django.http import JsonResponse
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from ..models import Investiment
from ..serializers import InvestimentSerializer


class InvestimentationViewSet(viewsets.ModelViewSet):
    queryset = Investiment.objects.all()
    serializer_class = InvestimentSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]

    # def create(self, request, *args, **kwargs):
    #     value = request.data.get('value', None)
    #     creation_date = request.data.get('creation_date', None)
    #     creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
    #     current_date = datetime.now()
    #     if creation_date > current_date:
    #         return JsonResponse({"Error": "Não pode se fazer um investimento com uma data futura"})

    #     if float(value) < 0:
    #         return JsonResponse({"Error": "O Valor não pode ser Negativo para a Criação do seu investimeto"})

    #     return super().create(request, *args, **kwargs)
    
    # def update(self, request, *args, **kwargs):
    #     value = request.data.get('value', None)
    #     creation_date = request.data.get('creation_date', None)

    #     creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
    #     current_date = datetime.now()
    #     if creation_date > current_date:
    #         return JsonResponse({"Error": "Não pode atualizar a data de cadastros do investimento  para uma data futura"})

    #     if float(value) < 0:
    #         return JsonResponse({"Error": "O Valor não pode ser Atualizado para um valor Negativo"})
    #     return super().update(request, *args, **kwargs)
