# Generated by Django 3.0.4 on 2020-05-29 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0016_edital_link_edital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='abertura',
            field=models.DateField(help_text='dd/mm/aaaa', null=True, verbose_name='Abertura do edital *'),
        ),
        migrations.AlterField(
            model_name='edital',
            name='descricao',
            field=models.CharField(max_length=200, verbose_name='Descrição *'),
        ),
        migrations.AlterField(
            model_name='edital',
            name='encerra',
            field=models.DateField(help_text='dd/mm/aaaa', null=True, verbose_name='Encerramento do edital *'),
        ),
        migrations.AlterField(
            model_name='edital',
            name='numero',
            field=models.CharField(max_length=20, verbose_name='Número do Edital *'),
        ),
    ]
