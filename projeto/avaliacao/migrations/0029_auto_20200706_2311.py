# Generated by Django 3.0.4 on 2020-07-07 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0028_auto_20200706_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='arquivo_parecer_final',
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='arquivo_parecer_comissao_final',
            field=models.FileField(blank=True, help_text='Use arquivo .pdf para a resposta', null=True, upload_to='midias', verbose_name='Arquivo de parecer SADEPI'),
        ),
    ]
