# Generated by Django 3.0.4 on 2020-06-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0013_auto_20200622_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='curso_graduacao_vinculado',
            field=models.CharField(help_text='Nome do curso que está lotado', max_length=50, verbose_name='Curso de Graduação vinculado'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='curso_pos_graduacao',
            field=models.CharField(blank=True, help_text='Caso esteja vinculado', max_length=50, null=True, verbose_name='Curso de Pós-graduação vinculado'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='grupo_pesquisa',
            field=models.CharField(blank=True, help_text='Caso esteja vinculado', max_length=100, null=True, verbose_name='Grupo de Pesquisa vinculado'),
        ),
    ]