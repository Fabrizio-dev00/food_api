from django.db import models

class Plato(models.Model):
    CATEGORIAS = [
        ('entrada', 'Entrada'),
        ('principal', 'Principal'),
        ('postre', 'Postre'),
        ('bebida', 'Bebida'),
    ]
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=30, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_preparacion', 'En preparación'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=30, choices=ESTADOS, default='pendiente')
    platos = models.ManyToManyField(Plato, related_name='pedidos', blank=True)

    def calcular_total(self):
        total = sum(p.precio for p in self.platos.all())
        self.total = total
        self.save(update_fields=['total'])
        return self.total

    def __str__(self):
        return f"Pedido {self.id} - {self.estado} - {self.fecha.date()}"
