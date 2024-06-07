from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.
class Programa(models.Model):
    nome = models.CharField(_(u'Descrição'), max_length=100)
    sigla = models.CharField('Sigla', max_length=20)
    tem_empresa_parceira = models.BooleanField(_(u'Tem empresas parceira'), default=False, help_text='Se marcado, obriga na submissão informar dados da empresa',blank=True)
    tem_instituicao_beneficiada = models.BooleanField(_(u'Tem instituição beneficiada'), default=False, help_text='Se marcado, obriga na submissão informar dados da instituição',blank=True)

    
    class Meta:
        ordering = ['sigla']

    def __str__(self):
        return self.sigla

    def save(self, *args, **kwargs):
        # self.nome = self.nome.upper()
        self.sigla = self.sigla.upper()
        super(Programa, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('programa_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('programa_delete', args=[str(self.id)])
