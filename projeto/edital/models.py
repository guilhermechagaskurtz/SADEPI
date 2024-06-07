from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from submissao.models import Submissao
from avaliacao.models import Avaliacao

class Edital(models.Model):
    numero = models.CharField(_(u'Número do Edital *'), max_length=20) #helptext='Disponibilizado no site do edital
    descricao = models.CharField(_(u'Descrição *'), max_length=200)
    orgao = models.ForeignKey('orgao.Orgao', verbose_name="Órgão de Fomento", on_delete=models.PROTECT)
    programa = models.ManyToManyField('programa.Programa',verbose_name='Programa(s) ou linha(s) de fomento', related_name='programa', help_text='Para selecionar ou deselecionar um programa pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse')
    abertura = models.DateField(_(u'Abertura do edital *'), blank = False , null = True, help_text='dd/mm/aaaa')
    encerra = models.DateField(_(u'Encerramento do edital *'), blank = False , null = True, help_text='dd/mm/aaaa')
    link_edital = models.URLField(_(u'Link do edital no site UFN'), help_text='Seção de editais do site UFN',blank=True)
    bolsista = models.BooleanField(_(u'bolsista'), default=False, help_text='Se marcado então há bolsista no edital',blank=True)
    
    
    class Meta:
        ordering = ['numero']

    def __str__(self):
        return '%s - %s - Encerramento: %s' % (self.orgao, self.numero, self.encerra.strftime('%d/%m/%Y'))

    def save(self, *args, **kwargs):
        self.numero = self.numero.upper()
        super(Edital, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('edital_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('edital_delete', args=[str(self.id)])
    
    @property
    def get_submissoes_todas_list_url(self):
        return reverse('submissao_edital_list', kwargs={'pk_edital': self.pk, 'situacao': 'TODAS'})

    @property
    def get_submissoes_aprovadas_list_url(self):
        return reverse('submissao_edital_list', kwargs={'pk_edital': self.pk, 'situacao':'APROVADAS'})

    @property
    def get_submissoes_reprovadas_list_url(self):
        return reverse('submissao_edital_list', kwargs={'pk_edital': self.pk, 'situacao': 'REPROVADAS'})

    @property
    def submissoes(self):
        return Submissao.objects.filter(edital=self)

    @property
    def submissoes_aprovadas(self):
        return self.submissoes.filter(id__in=[avaliacao.submissao.id for avaliacao in 
                                              Avaliacao.objects.filter(comissao__status='APROVADO', submissao__edital=self)])

    @property
    def submissoes_reprovadas(self):
        return self.submissoes.filter(id__in=[avaliacao.submissao.id for avaliacao in
                                              Avaliacao.objects.filter(comissao__status='REPROVADO', submissao__edital=self)])