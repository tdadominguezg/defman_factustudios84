from django.db import models


# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=45)
    razon_social = models.CharField(max_length=50, null=True, blank=True)
    nif = models.CharField(max_length=10, null=False)
    direccion = models.CharField(max_length=50)
    poblacion = models.CharField(max_length=15)
    codigo_postal = models.IntegerField(null=True)
    provincia = models.CharField(max_length=15)
    telefono = models.CharField(max_length=9)
    email = models.EmailField(null=True)
    IBAN = models.CharField(max_length=24, null=True, blank=True)


class Producto(models.Model):
    TYPES_CHOICES = [
        ('Audio', 'Audio'),
        ('Imagen', 'Imagen'),
        ('Video', 'Video'),
        ('Automocion', 'Automocion'),
        ('Grafico', 'Grafico'),
        ('Publicidad', 'Publicidad')
    ]

    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50)
    referencia = models.CharField(max_length=25, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    tipo = models.CharField(max_length=50, choices=TYPES_CHOICES)
    precio = models.FloatField()
    stock = models.IntegerField(blank=True, null=True)


class Factura(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=25, blank=True, null=True)
    fecha = models.DateField()
    vencimiento = models.DateField()
    producto = models.ManyToManyField(Producto, related_name="productos_factura")
    IVA = models.IntegerField()
    total = models.FloatField(blank=True, null=True)


class Albaran(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=25, blank=True, null=True)
    fecha = models.DateField()
    vencimiento = models.DateField()
    producto = models.ManyToManyField(Producto, related_name="productos_albaran")
    IVA = models.IntegerField()
    total = models.FloatField(blank=True, null=True)


class Presupuesto(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=25, null=False, blank=False)
    fecha = models.DateField()
    vencimiento = models.DateField()
    producto = models.ManyToManyField(Producto, related_name="producto_presupuesto")
    IVA = models.IntegerField()
    total = models.FloatField(blank=True, null=True)
