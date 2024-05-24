from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination
from ..models import Withdraw, Investiment
from ..serializers import WithdrawSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema

class PaginacaoWithdraw(PageNumberPagination):
    page_size = 10
    page_size_query_param = "limit"
    max_page_size = 1000

class WithdrawViewSet(viewsets.ModelViewSet):
    pagination_class = PaginacaoWithdraw
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = []

    @swagger_auto_schema(
        operation_description="Cria um novo saque.",
        responses={200: WithdrawSerializer()},
    )
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
    
    @swagger_auto_schema(
        operation_description="Atualiza um saque existente.",
        responses={200: WithdrawSerializer()},
    )
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
        super().update(request, *args, **kwargs)
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(
        operation_description="Exclui um saque.",
        responses={204: "No content"},
    )
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


    @swagger_auto_schema(
        operation_description="Retorna uma lista de todos os saques cadastrados.",
        responses={200: WithdrawSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna um saque pelo ID.",
        responses={200: WithdrawSerializer()},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Atualiza parcialmente um saque pelo ID (PATCH).",
        responses={200: WithdrawSerializer()},
    )
    def partial_update(self, request, *args, **kwargs):
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
        super().partial_update(request, *args, **kwargs)
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)