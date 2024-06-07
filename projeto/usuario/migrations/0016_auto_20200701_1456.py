# Generated by Django 3.0.4 on 2020-07-01 17:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0015_auto_20200629_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='pc_orientador_iniciacao_cientifica',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)], verbose_name='Quantidade de orientações de Iniciação científica/Tecnológica na UFN em andamento ou concluída (LIMITE 6):'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_orientador_mestrado',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Quantidade de dissertações de mestrado orientadas como orientador principal e aprovadas na UFN (LIMITE 5):'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_orientador_teses_doutorado',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Quantidade de teses de doutorado orientadas como orientador principal e aprovadas na UFN (LIMITE 5):'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_orientador_trabalho_final_curso',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)], verbose_name='Quantidade de orientações de Trabalho Final de Curso na UFN no estado concluído (LIMITE 6)'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_resumos_anais_eventos',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Quantidade de resumos ou resumos expandidos publicados em anais de eventos: (LIMITE 10):'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_trabalhos_anais_eventos',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Quantidade de trabalhos completos em anais de eventos (LIMITE 10)'),
        ),
    ]
