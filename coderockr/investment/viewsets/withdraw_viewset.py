from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from ..models import Withdraw, Investiment
from ..serializers import WithdrawSerializer
from django.http import JsonResponse
from datetime import datetime

class PaginacaoWithdraw(PageNumberPagination):
    page_size = 10
    page_query_param = 'limit'
    max_page_size = 1000
class WithdrawViewSet(viewsets.ModelViewSet):
    pagination_class = (PaginacaoWithdraw)
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]


    def create(self, request, *args, **kwargs):
        investiment = request.data.get('investment',None)
        value = request.data.get('value',None)
        withdrawal_date = request.data.get('withdrawal_date',None)
        withdraw_full_amount = request.data.get('withdraw_full_amount',None)
        withdrawal_date = datetime.strptime(withdrawal_date, '%Y-%m-%d')
        current_date = datetime.now()

        try:
            investiment = Investiment.objects.get(id=investiment)
        except:
            return JsonResponse({"Error": 'Investimento não encontrado, passe um investimento valido'})
        
        investment_date = str(investiment.creation_date)
        investment_date = datetime.strptime(investment_date, '%Y-%m-%d')

        if investiment.investment_withdrawal:
            return JsonResponse({"Error": 'Esse investimento ja foi retirado'})


        if withdraw_full_amount:
            value = investiment.saldo

        if float(value) < float(investiment.saldo):
            return JsonResponse({"Error": 'Não se pode fazer saque Parcial'})
        
        if withdrawal_date < investment_date:
            return JsonResponse({"Error": 'Não se pode fazer saque antes da data de criação do Investimento'})
        
        if withdrawal_date > current_date:
            return JsonResponse({"Error": 'Não se pode fazer saque em datas futuras'})

        return super().create(request, *args, **kwargs)
