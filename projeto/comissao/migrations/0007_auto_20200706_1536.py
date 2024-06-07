# Generated by Django 3.0.4 on 2020-07-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0006_auto_20200706_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comissao',
            name='status',
            field=models.CharField(choices=[('APROVADO', 'Aprovado'), ('REPROVADO', 'Reprovado'), ('EM ANÁLISE', 'Em análise')], default='EM ANÁLISE', max_length=25, verbose_name='Status do projeto'),
        ),
    ]
