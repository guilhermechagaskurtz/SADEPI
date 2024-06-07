from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.
class Orgao(models.Model):
    nome = models.CharField(_(u'Nome'), max_length=100)
    sigla = models.CharField('Sigla', max_length=20)
    site = models.CharField(_(u'Site do órgão de fomento'),max_length=100)

    
    class Meta:
        ordering = ['sigla']

    def __str__(self):
        return self.sigla

    def save(self, *args, **kwargs):
        # self.nome = self.nome.upper()
        self.sigla = self.sigla.upper()
        super(Orgao, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('orgao_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('orgao_delete', args=[str(self.id)])
