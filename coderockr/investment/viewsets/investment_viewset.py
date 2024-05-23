from django.http import JsonResponse
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from ..models import Investiment
from ..serializers import InvestimentSerializer
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination


class PaginacaoInvestment(PageNumberPagination):
    page_size = 10
    page_size_query_param = "limit"
    max_page_size = 1000

class InvestimentationViewSet(viewsets.ModelViewSet):
    pagination_class = (PaginacaoInvestment)
    queryset = Investiment.objects.all()
    serializer_class = InvestimentSerializer
    permission_classes = []

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]

    def create(self, request, *args, **kwargs):
        value = request.data.get('value', None)
        creation_date = request.data.get('creation_date', None)
        creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
        current_date = datetime.now()
        if creation_date > current_date:
            return JsonResponse({"Error": "Não pode se fazer um investimento com uma data futura"})

        if float(value) < 0:
            return JsonResponse({"Error": "O Valor não pode ser Negativo para a Criação do seu investimeto"})

        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        value = request.data.get('value', None)
        creation_date = request.data.get('creation_date', None)
        if creation_date:
            creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
            current_date = datetime.now()
            if creation_date > current_date:
                return JsonResponse({"Error": "Não pode atualizar a data de cadastros do investimento  para uma data futura"})

        if value and float(value) < 0:
            return JsonResponse({"Error": "O Valor não pode ser Atualizado para um valor Negativo"})
        
        date = creation_date if creation_date else instance.creation_date
        current_date = datetime.now() 
        months_passed = (current_date.year - date.year) * 12 + current_date.month - date.month
        
        # Se o dia atual for menor que o dia de criação, ajusta o número de meses
        if current_date.day < date.day:
            months_passed -= 1

        # Calcula o saldo acumulado multiplicando pelo fator mensal 0,52
        saldo = float(value)
        for _ in range(months_passed):
            saldo += saldo * 0.52

        instance.balance = round(saldo,2)
        instance.save()
        return super().update(request, *args, **kwargs)
    
        

        
