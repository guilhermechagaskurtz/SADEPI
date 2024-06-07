# Generated by Django 3.0.8 on 2020-07-27 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0023_auto_20200723_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissao',
            name='arquivo_apendice1',
            field=models.FileField(blank=True, help_text='Use este recurso em formato de imagem (png ou jpeg) com máximo de 50 MB', null=True, upload_to='midias', verbose_name='Apêndice ao projeto (pode ser usado para ilustrar algum processo metodológico ou no quadro do plano de trabalho).'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='introducao',
            field=models.TextField(help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!', max_length=3000, verbose_name='Introdução do projeto (3000 caracteres)'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='plano',
            field=models.TextField(help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!', max_length=2000, verbose_name='Plano de trabalho (lista de atividades e período de execução com no máximo 2000 caracteres). Se necessário, envie imagem do plano no Apêndice ao projeto'),
        ),
    ]
