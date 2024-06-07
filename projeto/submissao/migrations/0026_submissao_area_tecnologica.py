# Generated by Django 3.0.4 on 2020-09-01 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0025_auto_20200728_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissao',
            name='area_tecnologica',
            field=models.CharField(blank=True, choices=[('TECNOLOGIAS ESTRATÉGICAS', 'Tecnologias Estratégicas'), ('TECNOLOGIAS HABILITADORAS', 'Tecnologias Habilitadoras'), ('TECNOLOGIAS DE PRODUÇÃO', 'Tecnologias de Produção'), ('TECNOLOGIAS PARA O DESENVOLVIMENTO SUSTENTÁVEL', 'Tecnologias para o Desenvolvimento Sustentável'), ('TECNOLOGIAS PARA QUALIDADE DE VIDA', 'Tecnologias para Qualidade de Vida'), ('PESQUISA BÁSICA, HUMANIDADES E CIÊNCIAS SOCIAIS', 'Pesquisa básica, humanidades e ciências sociais')], help_text='Áreas de Tecnologias Prioritárias do Ministério da Ciência, Tecnologia, Inovações e Comunicações (MCTIC)', max_length=55, null=True, verbose_name='Área de aderência tecnológica'),
        ),
    ]