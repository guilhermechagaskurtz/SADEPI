# Generated by Django 3.0.8 on 2020-07-23 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0022_submissao_arquivo_apendice1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissao',
            name='arquivo_apendice1',
            field=models.FileField(blank=True, help_text='Use este recurso em formato de imagem (png ou jpeg)', null=True, upload_to='midias', verbose_name='Arquivo de apêndice ao projeto. Pode ser para ajudar na ilustração de algum processo metodológico ou no plano de trabalho.'),
        ),
    ]
