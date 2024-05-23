from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from ..models import Withdraw, Investiment
from ..serializers import WithdrawSerializer
from django.http import JsonResponse
from datetime import datetime

class PaginacaoWithdraw(PageNumberPagination):
    page_size = 10
    page_size_query_param = "limit"
    max_page_size = 1000

class WithdrawViewSet(viewsets.ModelViewSet):
    pagination_class = (PaginacaoWithdraw)
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer
    permission_classes = []

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
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        investiment = request.data.get('investment', instance.investment.id)
        value = request.data.get('value',None)
        withdrawal_date = request.data.get('withdrawal_date',instance.withdrawal_date)
        withdraw_full_amount = request.data.get('withdraw_full_amount',instance.withdraw_full_amount)
        withdrawal_date = datetime.strptime(withdrawal_date, '%Y-%m-%d')
        current_date = datetime.now()

        try:
            investiment = Investiment.objects.get(id=investiment)
        except:
            return JsonResponse({"Error": 'Investimento não encontrado, passe um investimento valido'})
        
        investment_date = str(investiment.creation_date)
        investment_date = datetime.strptime(investment_date, '%Y-%m-%d')

        if withdraw_full_amount:
            value = investiment.saldo

        if float(value) < float(investiment.saldo):
            return JsonResponse({"Error": 'Não se pode fazer saque Parcial'})
        
        if withdrawal_date < investment_date:
            return JsonResponse({"Error": 'Não se pode fazer saque antes da data de criação do Investimento'})
        
        if withdrawal_date > current_date:
            return JsonResponse({"Error": 'Não se pode fazer saque em datas futuras'})
        
        instance.value = instance.investment.saldo
        instance.save()

        investment = Investiment.objects.get(id=instance.investment.id)

        saldo = instance.valor_final - float(investment.value)

        investment.investment_withdrawal = True
        investment.balance = saldo
        investment.save()

        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        investiment = Investiment.objects.get(id=instance.investment.id)
        investiment.investment_withdrawal = False

        date = investiment.creation_date
        current_date = datetime.now() 
        months_passed = (current_date.year - date.year) * 12 + current_date.month - date.month
        
        # Se o dia atual for menor que o dia de criação, ajusta o número de meses
        if current_date.day < date.day:
            months_passed -= 1

        # Calcula o saldo acumulado multiplicando pelo fator mensal 0,52
        saldo = float(investiment.value)
        for _ in range(months_passed):
            saldo += saldo * 0.52

        investiment.balance = round(saldo,2)
        investiment.save()
        return super().destroy(request, *args, **kwargs)
