# Generated by Django 2.2.2 on 2020-04-15 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0017_auto_20190805_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='avaliador_responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='avaliador_responsavel', to=settings.AUTH_USER_MODEL, verbose_name='Selecione um professor como avaliador responsável *'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='avaliador_suplente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='avaliador_suplente', to=settings.AUTH_USER_MODEL, verbose_name='Selecione um professor como avaliador suplente'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='submissao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='submissao.Submissao', verbose_name='Selecione um projeto submetido para avaliação *'),
        ),
    ]
