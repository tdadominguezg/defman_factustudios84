from django.contrib import admin
from .models import Cliente, Producto, Presupuesto, Albaran, Factura
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(Cliente, ClienteAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(Producto, ProductoAdmin)

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'referencia','cliente')

admin.site.register(Factura, FacturaAdmin)

class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ('id', 'referencia', 'cliente')

admin.site.register(Presupuesto, PresupuestoAdmin)

class AlbaranAdmin(admin.ModelAdmin):
    list_display = ('id', 'referencia', 'cliente')

admin.site.register(Albaran, AlbaranAdmin)
