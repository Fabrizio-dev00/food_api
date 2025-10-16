from rest_framework import viewsets, filters
from django.db.models import Count
from .models import Plato, Pedido
from .serializers import PlatoSerializer, PedidoListSerializer, PedidoDetailSerializer

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all().annotate(pedidos_count=Count('pedidos'))
    serializer_class = PlatoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'categoria']
    ordering_fields = ['precio', 'nombre', 'pedidos_count']

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().prefetch_related('platos')
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['estado', 'platos__nombre']
    ordering_fields = ['fecha', 'total', 'estado']

    def get_serializer_class(self):
        if self.action in ['list', 'create']:
            return PedidoListSerializer
        return PedidoDetailSerializer
