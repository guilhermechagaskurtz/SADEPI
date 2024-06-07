from __future__ import unicode_literals

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.dispatch import receiver
from django.db.models import signals
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.utils import timezone

from avaliacao.models import Avaliacao
from comissao.models import Comissao


class Submissao(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS = (
        ('CIÊNCIAS DA SAÚDE', 'Ciências da Saúde'),
        ('CIÊNCIAS HUMANAS', 'Ciências Humanas' ),
        ('CIÊNCIAS SOCIAIS', 'Ciências Sociais'),
        ('CIÊNCIAS TECNOLÓGICAS', 'Ciências Tecnológicas' ),
    )

    PROGRAMAS_EXTENSAO = (
        ('ATENÇÃO INTEGRAL E PROMOÇÃO À SAÚDE', 'Atenção Integral e Promoção à Saúde'),
        ('EDUCAÇÃO, CULTURA E COMUNICAÇÃO', 'Educação, Cultura e Comunicação' ),
        ('DIREITOS, POLÍTICAS PÚBLICAS E DIVERSIDADE', 'Direitos, Políticas Públicas e Diversidade'),
        ('TECNOLOGIA, INOVAÇÃO E DESENVOLVIMENTO SUSTENTÁVEL', 'Tecnologia, Inovação e Desenvolvimento Sustentável' ),
        ('PATRIMÔNIO CULTURAL E ECONOMIA CRIATIVA', 'Patrimônio Cultural e Economia Criativa' ),
        ('SOCIEDADE E MEIO AMBIENTE', 'Sociedade e Meio Ambiente' ),
    )
    
    AREAS_ADERENCIA_TECNOLOGICA = (
        ('TECNOLOGIAS ESTRATÉGICAS','Tecnologias Estratégicas'),
        ('TECNOLOGIAS HABILITADORAS','Tecnologias Habilitadoras'),
        ('TECNOLOGIAS DE PRODUÇÃO','Tecnologias de Produção'),
        ('TECNOLOGIAS PARA O DESENVOLVIMENTO SUSTENTÁVEL','Tecnologias para o Desenvolvimento Sustentável'),
        ('TECNOLOGIAS PARA QUALIDADE DE VIDA','Tecnologias para Qualidade de Vida'),
        ('PESQUISA BÁSICA, HUMANIDADES E CIÊNCIAS SOCIAIS','Pesquisa básica, humanidades e ciências sociais'),
    )
     
    edital = models.ForeignKey('edital.Edital',verbose_name='Edital vigente *',null=True, blank=False, on_delete=models.PROTECT, help_text='Campo obrigatório como todos os que tiverem *')
    programa = models.ForeignKey('programa.Programa',verbose_name='Programa ou linha do edital *',null=True, blank=False, on_delete=models.PROTECT)    
    responsavel = models.ForeignKey('usuario.Usuario', verbose_name='Responsável pelo projeto (orientador) *',related_name='responsavel', null=False, blank=False, on_delete=models.PROTECT)
    colaborador = models.ManyToManyField('usuario.Usuario',verbose_name='Colaboradores (co-orientadores)', null=True, blank=True, related_name='colaborador')
    nome_empresa = models.CharField(_('Nome da empresa'),null=True,blank=True,max_length=100)
    contato_empresa = models.EmailField(_('Email da empresa'),unique=False,null=True,blank=True,max_length=100)
    area = models.CharField(_('Área de ensino, pesquisa e extensão de execução do projeto'), max_length=25, choices=TIPOS)
    programa_extensao = models.CharField(_('Programa Institucional de Extensão'), null=True, blank=True, max_length=55, choices=PROGRAMAS_EXTENSAO)
    area_tecnologica = models.CharField(_('Área de aderência tecnológica'), null=True, blank=True, max_length=55, choices=AREAS_ADERENCIA_TECNOLOGICA, help_text='Áreas de Tecnologias Prioritárias do Ministério da Ciência, Tecnologia, Inovações e Comunicações (MCTIC)')
    titulo = models.TextField(_('Título do projeto (200 caracteres)'), max_length=200, null=False, blank=False, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    introducao = models.TextField(_('Introdução do projeto (3000 caracteres)'),max_length=3000, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    palavras_chave = models.TextField(_('Palavras-chave: 3 a 5 expressões separadas por ponto-e-vírgula'), max_length=100, null=False, blank=False)
    motivacao = models.TextField(_('Justificativa do projeto (2000 caracteres)'), max_length=2000, null=False, blank=False, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    objetivo = models.TextField(_('Objetivos geral e específicos do projeto (2000 caracteres)'), max_length=2000, null=False, blank=False, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    metodologia = models.TextField(_('Materiais e Métodos do projeto (3000 caracteres)'), max_length=3000, null=False, blank=False, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    plano = models.TextField(_('Plano de trabalho (lista de atividades e período de execução com no máximo 2000 caracteres). Se necessário, envie imagem do plano no Apêndice ao projeto'), max_length=2000, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    referencia = models.TextField(_('Referências em ABNT (3000 caracteres)'), max_length=3000, null=False, blank=False, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    bolsista = models.ForeignKey('usuario.Usuario', related_name='bolsista', on_delete=models.PROTECT, null=True, blank=True, help_text='Atenção: solicite que o seu bolsista faça o cadastro no SISGEP-SADEPI')
    nome_instituicao_beneficiada = models.CharField(_('Nome da instituição beneficiada'), null=True, blank=True, max_length=100)
    contato_instituicao_beneficiada = models.EmailField(_(u'Email da instituição beneficiada'), unique=False, null=True, blank=True, max_length=100)
    cnpj_instituicao_beneficiada = models.CharField(_('CNPJ da instituição beneficiada'), null=True, blank=True, max_length=18)
    arquivo_apendice1 = models.FileField(_(u'Apêndice ao projeto (pode ser usado para ilustrar algum processo metodológico ou no quadro do plano de trabalho).'), blank=True, null=True, upload_to='midias', help_text='Use este recurso em formato de imagem (png ou jpeg) com máximo de 50 MB')


    class Meta:
        ordering = ['titulo', 'responsavel']
        unique_together = [['edital', 'responsavel']]

    def __str__(self):
        colaboradores = ''
        for c in self.colaborador.all():
            colaboradores += c.nome + ', '
        return '%s - %s - %s' % (self.titulo, self.responsavel, colaboradores)
    
    def save(self, *args, **kwargs):
        self.titulo = self.titulo.upper()
        if self.id:
            #no update
            submissao_pos_tratamento_final = Submissao.objects.get(id=self.id)
            
            # if self.get_status_avaliacao == 'PENDENTE':
            #     Avaliacao.objects.filter(submissao=self).update(status='PÓS CORREÇÃO')
            #     Comissao.objects.filter(avaliacao_comissao__submissao=self).update(status='PÓS CORREÇÃO')            
        super(Submissao, self).save(*args, **kwargs)

    @property
    def permite_alterar(self):
        return timezone.now().date() <= self.edital.encerra and not Avaliacao.objects.filter(submissao=self).exists()

    # @property
    # def get_status_avaliacao(self):
    #     obj = Avaliacao.objects.filter(submissao=self)
    #     if (len(obj) > 0):
    #         for c in obj:
    #             pass
    #         return c.status
    #     else: return 'EM EDIÇÃO'

    @property
    def permite_liberar_parecer(self):
        return 'APROVADO' == self.get_status_avaliacao or 'REPROVADO' == self.get_status_avaliacao
        
    @property
    def get_absolute_url(self):
        return reverse('submissao_update', args=[str(self.id)])
    
    @property
    def get_professor_absolute_url(self):
        return reverse('appprofessor_submissao_update', args=[str(self.id)])
    
    @property
    def get_absolute_url_pendente(self):
        return reverse('submissao_pendente_update', args=[str(self.id)])

    @property
    def get_avaliacao_responsavel_url(self):
        return reverse('appprofessor_minha_avaliacao_responsavel', args=[str(self.id)])

    @property
    def get_professor_delete_url(self):
        return reverse('appprofessor_submissao_delete', args=[str(self.id)])

    @property
    def get_avaliacao(self):
        try:
            return Avaliacao.objects.get(submissao=self)
        except:
            return None

    @property
    def get_avaliacao_create_update_url(self):
        """
            Se existe uma avaliacao para esta submissao,
            retornar a url de edicao desta avaliacao
            caso contrario, envia para a tela de criacao
            de uma avaliacao, passando o id da submissao como
            parametro GET
        """
        try:
            return self.get_avaliacao.get_absolute_url
        except:
            return '%s?submissao_id=%d' % (reverse('avaliacao_create'), self.id)

    @property
    def get_delete_url(self):
        return reverse('submissao_delete', args=[str(self.id)])

    @property
    def get_parecer_final(self):
        objetos = Comissao.objects.filter(avaliacao_comissao__submissao=self)
        if (objetos):
            return objetos[0].arquivo_parecer_comissao_final
        return None