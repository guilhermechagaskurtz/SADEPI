from __future__ import unicode_literals

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from decimal import Decimal

from comissao.models import Comissao


class Avaliacao(models.Model):
    submissao = models.OneToOneField('submissao.Submissao', verbose_name='Selecione um projeto submetido para avaliação *', null=False, blank=False, on_delete=models.PROTECT)
    avaliador_responsavel = models.ForeignKey('usuario.Usuario', verbose_name='Selecione um professor como avaliador responsável *', related_name='avaliador_responsavel', null=True, blank=True, on_delete=models.PROTECT)
    avaliador_suplente = models.ForeignKey('usuario.Usuario', verbose_name='Selecione um professor como avaliador suplente', related_name='avaliador_suplente', null=True, blank=True, on_delete=models.PROTECT)
    
    #Campos de parecer avaliador responsavel
    dt_avaliacao_responsavel = models.DateTimeField(_('Data da avaliação do responsável'), blank=True, null=True)
    parecer_avaliador_responsavel = models.TextField(_(u'Parecer do avaliador responsável (2000 caracteres)'), max_length=2000, null=True, blank=True, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    merito_projeto_relevancia_responsavel = models.DecimalField(_('O projeto apresentado tem caráter científico-investigativo, configurando um projeto de iniciação científica ou de inovação tecnológica, trazendo temas relevantes ou inovadores?'),help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)] , blank=True, null=True)
    merito_projeto_justificativa_responsavel = models.DecimalField(_('A justificativa é clara e tem relevância científica?'), help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], blank=True,null=True)
    merito_projeto_metodologia_responsavel = models.DecimalField(_('Os aspectos metodológicos do projeto envolvem os objetivos propostos?'), help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], blank=True,null=True)
    merito_projeto_plano_atividades_responsavel = models.DecimalField(_('O plano de atividades do bolsista contempla o projeto apresentado?'), help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],  blank=True,null=True)
    
    #Campos de parecer avaliador suplente
    dt_avaliacao_suplente = models.DateTimeField(_('Data da avaliação do suplente'), blank=True, null=True)
    parecer_avaliador_suplente = models.TextField(_(u'Parecer do avaliador suplente (2000 caracteres)'), max_length=2000, null=True, blank=True, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    merito_projeto_relevancia_suplente = models.DecimalField(_('O projeto apresentado tem caráter científico-investigativo, configurando um projeto de iniciação científica ou de inovação tecnológica, trazendo temas relevantes ou inovadores?'), help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)] , blank=True, null=True)
    merito_projeto_justificativa_suplente = models.DecimalField(_('A justificativa é clara e tem relevância científica?'), help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], blank=True,null=True)
    merito_projeto_metodologia_suplente = models.DecimalField(_('Os aspectos metodológicos do projeto envolvem os objetivos propostos?'), help_text='Máximo 1 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], blank=True,null=True)
    merito_projeto_plano_atividades_suplente = models.DecimalField(_('O plano de atividades do bolsista contempla o projeto apresentado?'), help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],  blank=True,null=True)

    pc_artigos_qualis_a1_cinco_autores = models.IntegerField(_('Quantidade de artigos Qualis A1 até 5 autores'),blank=True,null=True,default=0)
    pc_artigos_qualis_a1_mais_cinco_autores_primeiro_ultimo = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis A1 com mais de 5 autores: Primeiro ou último ator'),blank=True,null=True,default=0)
    pc_artigos_qualis_a1_mais_cinco_autores_demais = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis A1 com mais artigos até 5 autores: Demais posições de autoria'),blank=True,null=True,default=0)
    pc_artigos_qualis_a2_cinco_autores = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis A2 até 5 autores'),blank=True,null=True,default=0)
    pc_artigos_qualis_a2_mais_cinco_autores_primeiro_ultimo = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis A2 com mais de 5 autores: Primeiro ou último ator'),blank=True,null=True,default=0)
    pc_artigos_qualis_a2_mais_cinco_autores_demais = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis A2 com mais artigos até 5 autores: Demais posições de autoria'),blank=True,null=True,default=0)
    pc_artigos_qualis_b1_b2_cinco_autores = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis B1 e B2 até 5 autores'),blank=True,null=True,default=0)
    pc_artigos_qualis_b1_b2_mais_cinco_autores_primeiro_ultimo = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis B1 e B2 com mais de 5 autores: Primeiro ou último ator'),blank=True,null=True,default=0)
    pc_artigos_qualis_b1_b2_mais_cinco_autores_demais = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis B1 e B2 com mais artigos até 5 autores: Demais posições de autoria'),blank=True,null=True,default=0)
    pc_artigos_qualis_b3_b4_cinco_autores = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis B3 e B4 até 5 autores'),blank=True,null=True,default=0)
    pc_artigos_qualis_b3_b4_mais_cinco_autores_primeiro_ultimo = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis B3 e B4 com mais de 5 autores: Primeiro ou último ator'),blank=True,null=True,default=0)
    pc_artigos_qualis_b3_b4_mais_cinco_autores_demais = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis B3 e B4 com mais artigos até 5 autores: Demais posições de autoria'),blank=True,null=True,default=0)
    pc_artigos_qualis_b5_c_cinco_autores = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis B5 e C até 5 autores'),blank=True,null=True,default=0)
    pc_artigos_qualis_b5_c_mais_cinco_autores_primeiro_ultimo = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis B3 e C com mais de 5 autores: Primeiro ou último ator'),blank=True,null=True,default=0)
    pc_artigos_qualis_b5_c_mais_cinco_autores_demais = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de artigos Qualis B3 e C com mais artigos até 5 autores: Demais posições de autoria'),blank=True,null=True,default=0)
    pc_trabalhos_anais_eventos = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de trabalhos completos em anais de eventos (LIIMITE 10)'),validators=[MinValueValidator(0), MaxValueValidator(10)],blank=True,null=True,default=0)
    pc_resumos_anais_eventos = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de resumos ou resumos expandidos publicados em anais de eventos: (LIIMITE 10)'),validators=[MinValueValidator(0), MaxValueValidator(10)],blank=True,null=True,default = 0)
    pc_licenca_direito = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de licenças de direito de propriedade intelectual'),blank=True,null=True,default = 0)
    pc_autoria_livros = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de autoria de Livros Técnico/Científico com ISBN publicados em editora que possua ou Comitê, ou Comissão ou Conselho Editorial'),blank=True,null=True,default = 0)
    pc_autoria_livros_capitulos = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de capítulos e organização de Livros Técnico/Científico com ISBN publicados em editora que possua ou Comitê, ou Comissão ou Conselho Editorial'),blank=True,null=True,default = 0)
    pc_orientador_teses_doutorado = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de teses de doutorado orientadas como orientador principal e aprovadas na UFN (LIIMITE 5)'),validators=[MinValueValidator(0), MaxValueValidator(5)],blank=True,null=True,default = 0)
    pc_orientador_mestrado = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de dissertações de mestrado orientadas como orientador principal e aprovadas na UFN (LIIMITE 5)'),validators=[MinValueValidator(0), MaxValueValidator(5)],blank=True,null=True,default = 0)
    pc_orientador_iniciacao_cientifica = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de orientações de Iniciação científica/Tecnológica na UFN em andamento ou concluída (LIIMITE 6)'),validators=[MinValueValidator(0), MaxValueValidator(6)],blank=True,null=True,default = 0)
    pc_orientador_trabalho_final_curso = models.IntegerField(_('Produção Cientifíca dos últimos 3 anos - Quantidade de orientações de Trabalho Final de Curso na UFN no estado concluído: (LIIMITE 6)'),validators=[MinValueValidator(0), MaxValueValidator(6)],blank=True,null=True, default = 0)
    total_producoes = models.IntegerField(_('Total'), default = 0, blank=True, null=True)
    bolsista_media_notas = models.DecimalField(_('Bolsista - Média das notas do aluno nas disciplinas cursadas'), default = 0, help_text='Máximo 2.0 pontos', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(2.0)],  blank=True,null=True)
    

    class Meta:
        ordering = ['submissao', 'comissao__status']

    def __str__(self):
        return '%s' % (self.submissao)
    
    def save(self, *args, **kwargs):
        super(Avaliacao, self).save(*args, **kwargs)
    
    @property
    def get_absolute_url(self):
        return reverse('avaliacao_update', args=[str(self.id)])

    @property
    def get_avaliacao_responsavel_url(self):
        return reverse('appprofessor_minha_avaliacao_responsavel', args=[str(self.id)])

    @property
    def get_avaliacao_suplente_url(self):
        return reverse('appprofessor_minha_avaliacao_suplente', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('avaliacao_delete', args=[str(self.id)])

    @property
    def get_parecer(self):
        try:
            return Comissao.objects.get(avaliacao_comissao=self)
        except:
            return None

    @property
    def get_parecer_create_update_url(self):
        """
            Se existe um parecer na comissão para esta avaliação,
            retornar a url de edicao deste parecer
            caso contrario, envia para a tela de criacao
            de um parecer, passando o id da avaliacao como
            parametro GET
        """
        try:
            return self.get_parecer.get_absolute_url
        except:
            return '%s?avaliacao_id=%d' % (reverse('comissao_create'), self.id)

    @property
    def total_merito_projeto_responsavel(self):
        if self.merito_projeto_relevancia_responsavel == None:
            self.merito_projeto_relevancia_responsavel = 0
        if self.merito_projeto_justificativa_responsavel == None:
            self.merito_projeto_justificativa_responsavel = 0
        if self.merito_projeto_metodologia_responsavel == None:
            self.merito_projeto_metodologia_responsavel = 0
        if self.merito_projeto_plano_atividades_responsavel == None:
            self.merito_projeto_plano_atividades_responsavel = 0

        return self.merito_projeto_relevancia_responsavel + self.merito_projeto_justificativa_responsavel + self.merito_projeto_metodologia_responsavel + self.merito_projeto_plano_atividades_responsavel

    @property
    def total_merito_projeto_suplente(self):
        if self.merito_projeto_relevancia_suplente == None:
            self.merito_projeto_relevancia_suplente = 0
        if self.merito_projeto_justificativa_suplente == None:
            self.merito_projeto_justificativa_suplente = 0
        if self.merito_projeto_metodologia_suplente == None:
            self.merito_projeto_metodologia_suplente = 0
        if self.merito_projeto_plano_atividades_suplente == None:
            self.merito_projeto_plano_atividades_suplente = 0
        
        return self.merito_projeto_relevancia_suplente + self.merito_projeto_justificativa_suplente + self.merito_projeto_metodologia_suplente + self.merito_projeto_plano_atividades_suplente

    @property
    def media_merito_projeto(self):
        if (self.total_merito_projeto_suplente):
            return (self.total_merito_projeto_responsavel + self.total_merito_projeto_suplente) / 2
        return self.total_merito_projeto_responsavel

    @property
    def pontuacao_final_producoes(self):
        dicionario_pesos = {"pc_artigos_qualis_a1_cinco_autores" : 8,
                            "pc_artigos_qualis_a1_mais_cinco_autores_primeiro_ultimo" : 8,
                            "pc_artigos_qualis_a1_mais_cinco_autores_demais" : 6,
                            "pc_artigos_qualis_a2_cinco_autores" : 6,
                            "pc_artigos_qualis_a2_mais_cinco_autores_primeiro_ultimo" : 6,
                            "pc_artigos_qualis_a2_mais_cinco_autores_demais" : 4,
                            "pc_artigos_qualis_b1_b2_cinco_autores" : 4,
                            "pc_artigos_qualis_b1_b2_mais_cinco_autores_primeiro_ultimo" : 4,
                            "pc_artigos_qualis_b1_b2_mais_cinco_autores_demais" : 2,
                            "pc_artigos_qualis_b3_b4_cinco_autores" : 3,
                            "pc_artigos_qualis_b3_b4_mais_cinco_autores_primeiro_ultimo" : 3,
                            "pc_artigos_qualis_b3_b4_mais_cinco_autores_demais" : 1.5,
                            "pc_artigos_qualis_b5_c_cinco_autores" : 2,
                            "pc_artigos_qualis_b5_c_mais_cinco_autores_primeiro_ultimo" : 2,
                            "pc_artigos_qualis_b5_c_mais_cinco_autores_demais" : 1,
                            "pc_trabalhos_anais_eventos" : 0.2,
                            "pc_resumos_anais_eventos" : 0.1,
                            "pc_licenca_direito" : 3,
                            "pc_autoria_livros" : 4,
                            "pc_autoria_livros_capitulos" : 1, 
                            "pc_orientador_teses_doutorado" : 2,
                            "pc_orientador_mestrado" : 1,
                            "pc_orientador_iniciacao_cientifica" : 1,
                            "pc_orientador_trabalho_final_curso" : 0.5
        }
        
        return (self.submissao.responsavel.pc_artigos_qualis_a1_cinco_autores * dicionario_pesos["pc_artigos_qualis_a1_cinco_autores"] + self.submissao.responsavel.pc_artigos_qualis_a1_mais_cinco_autores_primeiro_ultimo * dicionario_pesos["pc_artigos_qualis_a1_mais_cinco_autores_primeiro_ultimo"] + self.submissao.responsavel.pc_artigos_qualis_a1_mais_cinco_autores_demais * dicionario_pesos["pc_artigos_qualis_a1_mais_cinco_autores_demais"] + self.submissao.responsavel.pc_artigos_qualis_a2_cinco_autores * dicionario_pesos["pc_artigos_qualis_a2_cinco_autores"] + self.submissao.responsavel.pc_artigos_qualis_a2_mais_cinco_autores_primeiro_ultimo * dicionario_pesos["pc_artigos_qualis_a2_mais_cinco_autores_primeiro_ultimo"] + self.submissao.responsavel.pc_artigos_qualis_a2_mais_cinco_autores_demais * dicionario_pesos["pc_artigos_qualis_a2_mais_cinco_autores_demais"] + self.submissao.responsavel.pc_artigos_qualis_b1_b2_cinco_autores * dicionario_pesos["pc_artigos_qualis_b1_b2_cinco_autores"] + self.submissao.responsavel.pc_artigos_qualis_b1_b2_mais_cinco_autores_primeiro_ultimo * dicionario_pesos["pc_artigos_qualis_b1_b2_mais_cinco_autores_primeiro_ultimo"] + self.submissao.responsavel.pc_artigos_qualis_b1_b2_mais_cinco_autores_demais * dicionario_pesos["pc_artigos_qualis_b1_b2_mais_cinco_autores_demais"] + self.submissao.responsavel.pc_artigos_qualis_b3_b4_cinco_autores * dicionario_pesos["pc_artigos_qualis_b3_b4_cinco_autores"] + self.submissao.responsavel.pc_artigos_qualis_b3_b4_mais_cinco_autores_primeiro_ultimo * dicionario_pesos["pc_artigos_qualis_b3_b4_mais_cinco_autores_primeiro_ultimo"] + self.submissao.responsavel.pc_artigos_qualis_b3_b4_mais_cinco_autores_demais * dicionario_pesos["pc_artigos_qualis_b3_b4_mais_cinco_autores_demais"] + self.submissao.responsavel.pc_artigos_qualis_b5_c_cinco_autores * dicionario_pesos["pc_artigos_qualis_b5_c_cinco_autores"] + self.submissao.responsavel.pc_artigos_qualis_b5_c_mais_cinco_autores_primeiro_ultimo * dicionario_pesos["pc_artigos_qualis_b5_c_mais_cinco_autores_primeiro_ultimo"] + self.submissao.responsavel.pc_artigos_qualis_b5_c_mais_cinco_autores_demais * dicionario_pesos["pc_artigos_qualis_b5_c_mais_cinco_autores_demais"] + self.submissao.responsavel.pc_trabalhos_anais_eventos * dicionario_pesos["pc_trabalhos_anais_eventos"] + self.submissao.responsavel.pc_resumos_anais_eventos * dicionario_pesos["pc_resumos_anais_eventos"] + self.submissao.responsavel.pc_licenca_direito * dicionario_pesos["pc_licenca_direito"] + self.submissao.responsavel.pc_autoria_livros * dicionario_pesos["pc_autoria_livros"] + self.submissao.responsavel.pc_autoria_livros_capitulos * dicionario_pesos["pc_autoria_livros_capitulos"] + self.submissao.responsavel.pc_orientador_teses_doutorado * dicionario_pesos["pc_orientador_teses_doutorado"] + self.submissao.responsavel.pc_orientador_mestrado * dicionario_pesos["pc_orientador_mestrado"] + self.submissao.responsavel.pc_orientador_iniciacao_cientifica * dicionario_pesos["pc_orientador_iniciacao_cientifica"] + self.submissao.responsavel.pc_orientador_trabalho_final_curso * dicionario_pesos["pc_orientador_trabalho_final_curso"])

    def get_dicionario_pesos(self, indice):
        dic_pesos = {
            "pc_artigos_qualis_a1_cinco_autores" : 8,
            "pc_artigos_qualis_a1_mais_cinco_autores_primeiro_ultimo" : 8,
            "pc_artigos_qualis_a1_mais_cinco_autores_demais" : 6,
            "pc_artigos_qualis_a2_cinco_autores" : 6,
            "pc_artigos_qualis_a2_mais_cinco_autores_primeiro_ultimo" : 6,
            "pc_artigos_qualis_a2_mais_cinco_autores_demais" : 4,
            "pc_artigos_qualis_b1_b2_cinco_autores" : 4,
            "pc_artigos_qualis_b1_b2_mais_cinco_autores_primeiro_ultimo" : 4,
            "pc_artigos_qualis_b1_b2_mais_cinco_autores_demais" : 2,
            "pc_artigos_qualis_b3_b4_cinco_autores" : 3,
            "pc_artigos_qualis_b3_b4_mais_cinco_autores_primeiro_ultimo" : 3,
            "pc_artigos_qualis_b3_b4_mais_cinco_autores_demais" : 1.5,
            "pc_artigos_qualis_b5_c_cinco_autores" : 2,
            "pc_artigos_qualis_b5_c_mais_cinco_autores_primeiro_ultimo" : 2,
            "pc_artigos_qualis_b5_c_mais_cinco_autores_demais" : 1,
            "pc_trabalhos_anais_eventos" : 0.2,
            "pc_resumos_anais_eventos" : 0.1,
            "pc_licenca_direito" : 3,
            "pc_autoria_livros" : 4,
            "pc_autoria_livros_capitulos" : 1, 
            "pc_orientador_teses_doutorado" : 2,
            "pc_orientador_mestrado" : 1,
            "pc_orientador_iniciacao_cientifica" : 1,
            "pc_orientador_trabalho_final_curso" : 0.5
        }
        return "xx"
        
    @property
    def pontuacao_final(self):
        nota_1 = Decimal(self.pontuacao_final_producoes * 4)
        nota_2 = self.media_merito_projeto * 4 
        nota_3 = self.bolsista_media_notas * 2 

        return (nota_1 + nota_2 + nota_3)/10

    @property
    def get_parecer_final(self):
        objetos = Comissao.objects.filter(avaliacao_comissao__submissao=self.submissao)
        if (objetos):
            return objetos[0].arquivo_parecer_comissao_final
        return None