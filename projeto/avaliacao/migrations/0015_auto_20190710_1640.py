# Generated by Django 2.2.2 on 2019-07-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0014_auto_20190710_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='pc_artigos_qualis_a1_cinco_autores',
            field=models.IntegerField(blank=True, default=5, null=True, verbose_name='Quantidade de artigos Qualis A1 até 5 autores'),
        ),
    ]
