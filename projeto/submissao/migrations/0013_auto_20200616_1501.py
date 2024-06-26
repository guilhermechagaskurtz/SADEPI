# Generated by Django 3.0.4 on 2020-06-16 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0021_auto_20200615_1826'),
        ('submissao', '0012_auto_20200601_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissao',
            name='programa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='programa_edital', to='edital.Edital', verbose_name='Programa ou linha do edital *'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='edital',
            field=models.ForeignKey(help_text='Campo obrigatório como todos os que tiverem *', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edital', to='edital.Edital', verbose_name='Edital vigente *'),
        ),
    ]
