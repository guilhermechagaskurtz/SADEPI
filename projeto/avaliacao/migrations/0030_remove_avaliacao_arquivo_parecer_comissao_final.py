# Generated by Django 3.0.4 on 2020-07-07 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0029_auto_20200706_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='arquivo_parecer_comissao_final',
        ),
    ]
