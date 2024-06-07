# Generated by Django 3.0.4 on 2020-06-17 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programa',
            name='tem_empresa_parceira',
            field=models.BooleanField(blank=True, default=False, help_text='Se marcado, obriga na submissão informar dados da empresa', verbose_name='Tem empresas parceira'),
        ),
        migrations.AddField(
            model_name='programa',
            name='tem_instituicao_beneficiada',
            field=models.BooleanField(blank=True, default=False, help_text='Se marcado, obriga na submissão informar dados da instituição', verbose_name='Tem instituição beneficiada'),
        ),
    ]
