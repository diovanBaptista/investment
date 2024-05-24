from rest_framework import filters, viewsets
from django.contrib.auth.models import User
from ..models import Investor
from ..serializers import InvestorSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from drf_yasg import openapi

class PaginacaoInvestor(PageNumberPagination):
    page_size = 10
    page_size_query_param = "limit"
    max_page_size = 1000

class InvestorViewSet(viewsets.ModelViewSet):
    pagination_class = (PaginacaoInvestor)
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = []

    @swagger_auto_schema(operation_description="Esta operação permite criar um novo investidor fornecendo informações de usuário, nome completo e CPF. O usuário será registrado com um nome de usuário único, um endereço de e-mail válido e uma senha. O investidor será associado ao usuário criado.")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    @swagger_auto_schema(operation_description="Recupera um investidor pelo ID")
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Atualiza um investidor e usuário pelo ID. Os seguintes campos podem ser atualizados: 'username', 'email', 'password', 'name' e 'cpf'.",
        responses={200: 'Success'},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Novo nome de usuário'),
                        'email': openapi.Schema(type=openapi.TYPE_STRING, format='email', description='Novo endereço de e-mail'),
                        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Nova senha'),
                    }
                ),
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Novo nome do investidor'),
                'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='Novo CPF do investidor'),
            },
            required=['user', 'name', 'cpf']
        )
    )
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Atualiza parcialmente um investidor e usuário pelo ID (PATCH). Os seguintes campos podem ser atualizados: 'username', 'email', 'password', 'name' e 'cpf'.",
        responses={200: 'Success'},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Novo nome de usuário'),
                        'email': openapi.Schema(type=openapi.TYPE_STRING, format='email', description='Novo endereço de e-mail'),
                        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Nova senha'),
                    }
                ),
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Novo nome do investidor'),
                'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='Novo CPF do investidor'),
            },
        )
    )
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="Exclui um investidor pelo ID")
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = User.objects.get(id=instance.user.id)
        user.delete()
        self.perform_destroy(instance)
        return Response(status=200)

    @swagger_auto_schema(operation_description="Lista todos os investidores")
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

  