# Generated by Django 3.0.4 on 2020-06-01 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0009_auto_20200415_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='area_conhecimento_cnpq',
            field=models.CharField(max_length=50, verbose_name='Área de conhecimento no CNPq'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=14, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rg',
            field=models.IntegerField(verbose_name='RG'),
        ),
    ]
