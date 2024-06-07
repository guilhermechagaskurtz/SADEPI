# Generated by Django 2.1.2 on 2018-12-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20, verbose_name='Número do Edital')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('abertura', models.CharField(max_length=20, verbose_name='Abertura do edital')),
                ('encerra', models.CharField(max_length=20, verbose_name='Encerramento do edital')),
            ],
            options={
                'ordering': ['numero'],
            },
        ),
    ]
