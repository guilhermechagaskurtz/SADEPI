# Generated by Django 2.2.1 on 2019-06-12 19:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0008_auto_20190612_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='atividades_cientificas_orientador_eventos_anais_completo',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(0.4)], verbose_name='Atividades Científicas 2015-2018 - Trabalho completo em anais de evento: primeiro ou último autor (0.05), demais posições (0.01)'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='atividades_cientificas_orientador_eventos_resumos',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(0.3)], verbose_name='Atividades Científicas 2015-2018 - Resumos em eventos: primeiro ou último autor (0.02), demais posições (0.01)'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='atividades_cientificas_orientador_livros',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(0.3)], verbose_name='Atividades Científicas 2015-2018 - Livros: capitulo de livros (0.1), livro completo (0.2)'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='atividades_cientificas_orientador_revista_internacional',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Atividades Científicas 2015-2018 - Publicação em revista internacional: primeiro ou último ator (0.4), demais posições (0.2)'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='atividades_cientificas_orientador_revista_nacional',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Atividades Científicas 2015-2018 - Publicação em revista nacional com Qualis: primeiro ou último autor: (0.20), demais posições (0.10) '),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='atividades_cientificas_orientador_strict_sisu',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(0.5)], verbose_name='Atividades Científicas 2015-2018 - O orientador é bolsistar de produtividade CNPQ? (máximo 0.1pontos)'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='merito_projeto_relevancia',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Mérito do projeto - O projeto apresentado tem caráter científico-investigativo, configurando um projeto de iniciação científica, trazendo temas relevantes ou inovadores? (máximo 1.0 ponto)'),
        ),
    ]
