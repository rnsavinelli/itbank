# Generated by Django 4.1 on 2022-08-29 02:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'DIRECCIONES',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.address')),
            ],
            options={
                'db_table': 'SUCURSALES',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('C', 'Classic'), ('G', 'Gold'), ('B', 'Black')], default='C', max_length=1)),
                ('dni', models.IntegerField(null=True)),
                ('dob', models.CharField(max_length=200, null=True)),
                ('address', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.address')),
                ('branch', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.branch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'CLIENTES',
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('MO', 'Mortgage'), ('PE', 'Personal'), ('PL', 'Pledge')], max_length=2)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('total', models.FloatField()),
                ('cancelled', models.FloatField(default=0.0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.cliente')),
            ],
            options={
                'db_table': 'PRESTAMOS',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.PositiveIntegerField(unique=True)),
                ('hire_date', models.DateField(default=datetime.date.today)),
                ('address', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.address')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.branch')),
                ('user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'EMPLEADOS',
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('CA', 'Current Account'), ('SA', 'Savings Account'), ('SAU', 'Savings Account (USD)')], default='CA', max_length=3)),
                ('iban', models.CharField(default='-', max_length=200, null=True)),
                ('balance', models.FloatField(default=0.0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'CUENTAS',
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('D', 'Debit'), ('C', 'Credit'), ('G', 'Gift')], default='D', max_length=1)),
                ('brand', models.CharField(choices=[('VISA', 'Visa'), ('MASTERCARD', 'Mastercard'), ('AMEX', 'American Express')], default='VISA', max_length=25)),
                ('number', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=4)),
                ('valid_from', models.DateField(auto_now=True)),
                ('expiration_end', models.DateField(editable=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TARJETAS',
                'unique_together': {('number', 'cvv')},
            },
        ),
    ]