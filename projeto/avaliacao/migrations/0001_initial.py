# Generated by Django 2.2.1 on 2019-05-22 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submissao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('APROVADO', 'Aprovado'), ('REPROVADO', 'Reprovado'), ('EM ANÁLISE', 'Em análise'), ('EM EDIÇÃO', 'Em edição')], max_length=25, verbose_name='Status do projeto')),
                ('parecer_avaliador_responsavel', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Parecer do avaliador responsável (2000 caracteres)')),
                ('parecer_avaliador_suplente', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Parecer do avaliador suplente (2000 caracteres)')),
                ('avaliador_responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='avaliador_responsavel', to=settings.AUTH_USER_MODEL)),
                ('avaliador_suplente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='avaliador_suplente', to=settings.AUTH_USER_MODEL)),
                ('submissao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='submissao.Submissao')),
            ],
            options={
                'ordering': ['submissao', 'status'],
            },
        ),
    ]
