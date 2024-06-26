# Generated by Django 3.0.4 on 2020-07-01 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submissao', '0016_auto_20200619_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissao',
            name='colaborador',
            field=models.ManyToManyField(blank=True, null=True, related_name='colaborador', to=settings.AUTH_USER_MODEL, verbose_name='Colaboradores (co-orientadores)'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='motivacao',
            field=models.TextField(max_length=2000, verbose_name='Justificativa do projeto (2000 caracteres)'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='plano',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Plano de trabalho'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responsavel', to=settings.AUTH_USER_MODEL, verbose_name='Responsável pelo projeto (orientador) *'),
        ),
    ]
