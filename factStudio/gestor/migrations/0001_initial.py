# Generated by Django 3.2 on 2022-10-23 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=45)),
                ('razon_social', models.CharField(max_length=50, null=True)),
                ('nif', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=50)),
                ('poblacion', models.CharField(max_length=15)),
                ('codigo_postal', models.IntegerField(null=True)),
                ('provincia', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('IBAN', models.CharField(max_length=24, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('referencia', models.CharField(max_length=25)),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('referencia', models.CharField(max_length=25)),
                ('fecha', models.DateField()),
                ('IVA', models.IntegerField()),
                ('total', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.cliente')),
                ('producto', models.ManyToManyField(related_name='producto_presupuesto', to='gestor.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('referencia', models.CharField(max_length=25)),
                ('IVA', models.IntegerField()),
                ('total', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.cliente')),
                ('producto', models.ManyToManyField(related_name='productos_factura', to='gestor.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Albaran',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('referencia', models.CharField(max_length=25)),
                ('fecha', models.DateField()),
                ('vencimiento', models.DateField()),
                ('IVA', models.IntegerField()),
                ('total', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.cliente')),
                ('producto', models.ManyToManyField(related_name='productos_albaran', to='gestor.Producto')),
            ],
        ),
    ]