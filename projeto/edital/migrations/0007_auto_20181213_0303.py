# Generated by Django 2.1.2 on 2018-12-13 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0006_auto_20181213_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='numero',
            field=models.CharField(help_text='Disponibilizado no site do edital', max_length=20, verbose_name='Número do Edital'),
        ),
    ]
