# Generated by Django 3.0.4 on 2020-06-01 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submissao', '0011_auto_20200601_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissao',
            name='colaborador',
            field=models.ManyToManyField(blank=True, help_text='Para selecionar ou deselecionar um colaborador pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse', null=True, related_name='colaborador', to=settings.AUTH_USER_MODEL, verbose_name='Colaborador(es)'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responsavel', to=settings.AUTH_USER_MODEL, verbose_name='Responsável pelo projeto *'),
        ),
    ]
