# Generated by Django 2.1.2 on 2019-03-12 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituicao',
            name='contato',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nome Completo do contato'),
        ),
    ]
