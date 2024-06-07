# Generated by Django 3.0.4 on 2020-09-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0010_auto_20200707_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='comissao',
            name='comentario',
            field=models.TextField(blank=True, help_text='Digite todo e qualquer comentário ou anotação pertinente', null=True, verbose_name='Comentários'),
        ),
        migrations.AddField(
            model_name='comissao',
            name='dt_trancado',
            field=models.DateField(blank=True, null=True, verbose_name='Data de trancamento do projeto'),
        ),
        migrations.AlterField(
            model_name='comissao',
            name='status',
            field=models.CharField(choices=[('APROVADO', 'Aprovado'), ('REPROVADO', 'Reprovado'), ('EM ANÁLISE', 'Em análise'), ('TRANCADO', 'Trancado')], default='EM ANÁLISE', max_length=25, verbose_name='Status final do projeto'),
        ),
    ]