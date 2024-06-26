# Generated by Django 3.0.4 on 2020-07-02 22:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0016_auto_20200701_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_a1_cinco_autores',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade de artigos Qualis A1 até 5 autores'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_a1_mais_cinco_autores_demais',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis A1 com mais artigos até 5 autores: Demais posições de autoria'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_a1_mais_cinco_autores_primeiro_ultimo',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis A1 com mais de 5 autores: Primeiro ou último ator'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_a2_cinco_autores',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis A2 até 5 autores'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_a2_mais_cinco_autores_demais',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis A2 com mais artigos até 5 autores: Demais posições de autoria'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_a2_mais_cinco_autores_primeiro_ultimo',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis A2 com mais de 5 autores: Primeiro ou último ator'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_b1_b2_cinco_autores',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis B1 e B2 até 5 autores'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_b1_b2_mais_cinco_autores_demais',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis B1 e B2 com mais artigos até 5 autores: Demais posições de autoria'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_b1_b2_mais_cinco_autores_primeiro_ultimo',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis B1 e B2 com mais de 5 autores: Primeiro ou último ator'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_b3_b4_cinco_autores',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis B3 e B4 até 5 autores'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_b3_b4_mais_cinco_autores_demais',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis B3 e B4 com mais artigos até 5 autores: Demais posições de autoria'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_b3_b4_mais_cinco_autores_primeiro_ultimo',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis B3 e B4 com mais de 5 autores: Primeiro ou último ator'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_b5_c_cinco_autores',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis B5 e C até 5 autores'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_b5_c_mais_cinco_autores_demais',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis B3 e C com mais artigos até 5 autores: Demais posições de autoria'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_artigos_qualis_b5_c_mais_cinco_autores_primeiro_ultimo',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de artigos Qualis B3 e C com mais de 5 autores: Primeiro ou último ator'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_autoria_livros',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de autoria de Livros Técnico/Científico com ISBN publicados em editora que possua ou Comitê, ou Comissão ou Conselho Editorial'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_autoria_livros_capitulos',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de capítulos e organização de Livros Técnico/Científico com ISBN publicados em editora que possua ou Comitê, ou Comissão ou Conselho Editorial'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_licenca_direito',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de licenças de direito de propriedade intelectual'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_orientador_iniciacao_cientifica',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)], verbose_name='Quantidade de orientações de Iniciação científica/Tecnológica na UFN em andamento ou concluída (LIMITE 6):'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_orientador_mestrado',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Quantidade de dissertações de mestrado orientadas como orientador principal e aprovadas na UFN (LIMITE 5):'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_orientador_teses_doutorado',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Quantidade de teses de doutorado orientadas como orientador principal e aprovadas na UFN (LIMITE 5):'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_orientador_trabalho_final_curso',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)], verbose_name='Quantidade de orientações de Trabalho Final de Curso na UFN no estado concluído (LIMITE 6)'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_resumos_anais_eventos',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Quantidade de resumos ou resumos expandidos publicados em anais de eventos: (LIMITE 10):'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pc_trabalhos_anais_eventos',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Quantidade de trabalhos completos em anais de eventos (LIMITE 10)'),
        ),
    ]
