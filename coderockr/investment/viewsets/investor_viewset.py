from rest_framework import filters, viewsets
from django.contrib.auth.models import User
from ..models import Investor
from ..serializers import InvestorSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

class InvestorViewSet(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = []

    @swagger_auto_schema(operation_description="Cria um novo investidor")
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

    @swagger_auto_schema(operation_description="Atualiza um investidor pelo ID")
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Atualiza parcialmente um investidor pelo ID (PATCH)")
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

  