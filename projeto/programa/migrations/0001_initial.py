# Generated by Django 3.0.4 on 2020-06-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Descrição')),
                ('sigla', models.CharField(max_length=20, verbose_name='Sigla')),
            ],
            options={
                'ordering': ['sigla'],
            },
        ),
    ]
