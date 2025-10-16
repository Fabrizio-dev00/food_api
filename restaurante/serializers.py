from rest_framework import serializers
from .models import Plato, Pedido

class PlatoSerializer(serializers.ModelSerializer):
    pedidos_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Plato
        fields = ['id', 'nombre', 'precio', 'categoria', 'pedidos_count']

class PedidoListSerializer(serializers.ModelSerializer):
    platos = serializers.PrimaryKeyRelatedField(queryset=Plato.objects.all(), many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'fecha', 'total', 'estado', 'platos']

class PedidoDetailSerializer(serializers.ModelSerializer):
    platos = PlatoSerializer(many=True, read_only=True)
    platos_ids = serializers.PrimaryKeyRelatedField(write_only=True, many=True, source='platos', queryset=Plato.objects.all())

    class Meta:
        model = Pedido
        fields = ['id', 'fecha', 'total', 'estado', 'platos', 'platos_ids']

    def create(self, validated_data):
        platos = validated_data.pop('platos', [])
        pedido = Pedido.objects.create(**validated_data)
        pedido.platos.set(platos)
        pedido.calcular_total()
        return pedido

    def update(self, instance, validated_data):
        platos = validated_data.pop('platos', None)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        if platos is not None:
            instance.platos.set(platos)
            instance.calcular_total()
        return instance
