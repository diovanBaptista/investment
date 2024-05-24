from django.http import JsonResponse
from rest_framework import filters, viewsets
from datetime import datetime
from ..models import Investiment
from ..serializers import InvestimentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
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

    search_fields = []

    def validate_and_calculate_balance(self, instance, value, creation_date):
        # Validate creation date
        if creation_date:
            creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
            current_date = datetime.now()
            if creation_date > current_date:
                return {"Error": "Não pode atualizar a data de cadastros do investimento para uma data futura"}

        # Validate value
        if value and float(value) <= 0:
            return {"Error": "O Valor não pode ser Atualizado para um valor Negativo"}
        
        # Calculate balance
        date = creation_date if creation_date else instance.creation_date
        current_date = datetime.now()
        months_passed = (current_date.year - date.year) * 12 + current_date.month - date.month
        
        # Adjust the number of months if the current day is less than the creation day
        if current_date.day < date.day:
            months_passed -= 1

        # Calculate the accumulated balance
        saldo = float(value)
        for _ in range(months_passed):
            saldo += saldo * 0.52

        instance.balance = round(saldo, 2)
        return None
    
    @swagger_auto_schema(
        operation_description="Retorna uma lista de todos os investidores cadastrados.",
        responses={200: 'Success'},
    )
    def list(self, request):
        investments = Investiment.objects.all()
        serializer = InvestimentSerializer(investments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Esta operação permite criar um novo investimento fornecendo informações como o valor do investimento, a data de criação, o status de retirada de investimento e o proprietário associado. Ao criar o investimento, o saldo é automaticamente calculado com base na data de criação do investimento e nos juros compostos de 0,52% ao mês até o mês atual. As seguintes validações são aplicadas: O valor do investimento não pode ser negativo ou igual a zero. A data de criação não pode ser uma data futura.",
        responses={200: 'Success'},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'value': openapi.Schema(type=openapi.TYPE_NUMBER, format='float', description='Valor do investimento'),
                'creation_date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Data de criação do investimento (formato: YYYY-MM-DD)'),
                'owner': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID do proprietário do investimento'),
            },
            required=['value', 'creation_date', 'owner']
        )
    )
    def create(self, request, *args, **kwargs):
        value = request.data.get('value', None)
        creation_date = request.data.get('creation_date', None)
        creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
        current_date = datetime.now()
        if creation_date > current_date:
            return JsonResponse({"Error": "Não pode se fazer um investimento com uma data futura"})

        if float(value) <= 0:
            return JsonResponse({"Error": "O Valor não pode ser Negativo ou igual a 0 para a Criação do seu investimeto"})
        
        response = super().create(request, *args, **kwargs)

        return response
    
    @swagger_auto_schema(
        operation_description="Retorna um investimento pelo ID.",
        responses={200: InvestimentSerializer()},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Atualiza parcialmente um investimento pelo ID (PATCH). Ao atualizar parcialmente o investimento, o saldo é recalculado com base na nova data de criação, se fornecida, e nos juros compostos de 0,52% ao mês até o mês atual. As seguintes validações são aplicadas: O valor do investimento não pode ser negativo ou igual a zero. A nova data de criação não pode ser uma data futura.",
        responses={200: InvestimentSerializer()},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'value': openapi.Schema(type=openapi.TYPE_NUMBER, format='float', description='Novo valor do investimento'),
                'creation_date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Nova data de criação do investimento (formato: YYYY-MM-DD)'),
                'owner': openapi.Schema(type=openapi.TYPE_INTEGER, description='Novo ID do proprietário do investimento'),
            },
        )
    )
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        value = request.data.get('value', instance.value)
        creation_date = request.data.get('creation_date', instance.creation_date)
        creation_date = f"{creation_date}"

        error_response = self.validate_and_calculate_balance(instance, value, creation_date)
        if error_response:
            return JsonResponse(error_response)

        instance.save()
        super().partial_update(request, *args, **kwargs)
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Atualiza completamente um investimento pelo ID (PUT). Ao atualizar completamente o investimento, o saldo é recalculado com base na nova data de criação, se fornecida, e nos juros compostos de 0,52% ao mês até o mês atual. As seguintes validações são aplicadas: O valor do investimento não pode ser negativo ou igual a zero. A nova data de criação não pode ser uma data futura.",
        responses={200: InvestimentSerializer()},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'value': openapi.Schema(type=openapi.TYPE_NUMBER, format='float', description='Novo valor do investimento'),
                'creation_date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Nova data de criação do investimento (formato: YYYY-MM-DD)'),
                'owner': openapi.Schema(type=openapi.TYPE_INTEGER, description='Novo ID do proprietário do investimento'),
            },
            required=['value', 'creation_date', 'owner']
        )
    )
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        value = request.data.get('value', instance.value)
        creation_date = request.data.get('creation_date', instance.creation_date)
        creation_date = f"{creation_date}"

        error_response = self.validate_and_calculate_balance(instance, value, creation_date)
        if error_response:
            return JsonResponse(error_response)

        instance.save()
        super().update(request, *args, **kwargs)
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Esss Rota ele excluio investimento passando o id",
        responses={204: openapi.Response(description="No content")},
    )
    def destroy(self, request, pk=None, **kwargs):
        try:
            investment = Investiment.objects.get(id=pk)
            investment.delete()
            return Response(status=204)
        except Investiment.DoesNotExist:
            return Response({"detail": "Investimento não encontrado."}, status=404)
