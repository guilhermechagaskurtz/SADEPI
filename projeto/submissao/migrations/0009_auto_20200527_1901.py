# Generated by Django 3.0.4 on 2020-05-27 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0008_auto_20200522_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submissao',
            name='arquivo_atualizacao_pendencia_projeto',
        ),
        migrations.RemoveField(
            model_name='submissao',
            name='arquivo_projeto',
        ),
    ]
