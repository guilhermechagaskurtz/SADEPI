# Generated by Django 2.1.2 on 2018-12-13 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0007_auto_20181213_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='abertura',
            field=models.CharField(max_length=20, verbose_name='Abertura do edital'),
        ),
        migrations.AlterField(
            model_name='edital',
            name='encerra',
            field=models.CharField(max_length=20, verbose_name='Encerramento do edital'),
        ),
        migrations.AlterField(
            model_name='edital',
            name='numero',
            field=models.CharField(max_length=20, verbose_name='Número do Edital'),
        ),
    ]
