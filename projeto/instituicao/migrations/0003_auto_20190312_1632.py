# Generated by Django 2.1.2 on 2019-03-12 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0002_instituicao_contato'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituicao',
            name='email',
            field=models.EmailField(blank=True, max_length=100, verbose_name='Email do contato'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='telefone',
            field=models.CharField(blank=True, max_length=100, verbose_name='Telefone do contato'),
        ),
        migrations.AlterField(
            model_name='instituicao',
            name='contato',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nome completo do contato'),
        ),
    ]