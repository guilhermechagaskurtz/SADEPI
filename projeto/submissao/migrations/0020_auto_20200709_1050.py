# Generated by Django 3.0.4 on 2020-07-09 13:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0021_auto_20200615_1826'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submissao', '0019_auto_20200701_1800'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='submissao',
            unique_together={('edital', 'responsavel')},
        ),
    ]
