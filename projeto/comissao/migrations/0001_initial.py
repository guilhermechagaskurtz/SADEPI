# Generated by Django 2.2.2 on 2020-04-15 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('avaliacao', '0018_auto_20200415_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comissao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parecer_comissao', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Parecer da comissão (2000 caracteres)')),
                ('dt_avaliacao_comissao', models.DateTimeField(blank=True, null=True, verbose_name='Data da avaliação da comissão')),
                ('status', models.CharField(choices=[('APROVADO', 'Aprovado'), ('REPROVADO', 'Reprovado'), ('EM ANÁLISE', 'Em análise')], max_length=25, verbose_name='Status do projeto')),
                ('arquivo_resposta_comissao', models.FileField(help_text='Use arquivo .pdf para a resposta', upload_to='midias', verbose_name='Arquivo padrão de resposta a submissão do projeto *')),
                ('avaliacao_comissao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='avaliacao.Avaliacao', verbose_name='Selecione uma avaliação de projeto submetido para parecer da comissão *')),
            ],
            options={
                'ordering': ['avaliacao_comissao', 'status'],
            },
        ),
    ]