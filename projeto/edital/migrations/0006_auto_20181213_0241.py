# Generated by Django 2.1.2 on 2018-12-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0005_auto_20181213_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='abertura',
            field=models.DateField(verbose_name='Abertura do edital'),
        ),
    ]
