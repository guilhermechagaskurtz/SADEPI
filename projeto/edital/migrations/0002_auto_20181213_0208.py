# Generated by Django 2.1.2 on 2018-12-13 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='abertura',
            field=models.DateField(max_length=20, verbose_name='Abertura do edital'),
        ),
        migrations.AlterField(
            model_name='edital',
            name='encerra',
            field=models.DateField(max_length=20, verbose_name='Encerramento do edital'),
        ),
    ]
