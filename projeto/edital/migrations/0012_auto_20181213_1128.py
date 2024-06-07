# Generated by Django 2.1.2 on 2018-12-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0011_auto_20181213_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='abertura',
            field=models.DateField(blank=True, help_text='Ex.:01/01/2010', max_length=10, null=True, verbose_name='Abertura do edital'),
        ),
        migrations.AlterField(
            model_name='edital',
            name='encerra',
            field=models.DateField(blank=True, help_text='Ex.:01/01/2010', max_length=10, null=True, verbose_name='Encerramento do edital'),
        ),
    ]
