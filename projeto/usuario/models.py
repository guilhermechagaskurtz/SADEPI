from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from datetime import timedelta, datetime

from utils.gerador_hash import gerar_hash


class AdministradorAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='ADMINISTRADOR', is_active=True)


class ProfessorAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='PROFESSOR', is_active=True) 


class BolsistaAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='BOLSISTA', is_active=True)


class BolsistaInativoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='BOLSISTA', is_active=False)


class Usuario(AbstractBaseUser):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS = (
        ('ADMINISTRADOR', 'Administrador'),
        ('PROFESSOR', 'Professor' ),
        ('BOLSISTA', 'Bolsista')
    )
    AREAS = (
        ('CIÊNCIAS DA SAÚDE', 'Ciências da Saúde'),
        ('CIÊNCIAS HUMANAS', 'Ciências Humanas' ),
        ('CIÊNCIAS SOCIAIS', 'Ciências Sociais'),
        ('CIÊNCIAS TECNOLÓGICAS', 'Ciências Tecnológicas' ),
    )

    USERNAME_FIELD = 'email'

    tipo = models.CharField(_('Tipo do usuário *'), max_length=15, choices=TIPOS, default='PROFESSOR', help_text='* Campos obrigatórios')
    nome = models.CharField(_('Nome completo *'), max_length=100)
    email = models.EmailField(_('Email'), unique=True, max_length=100, db_index=True)
    data_nasc = models.DateField(_('Data de Nascimento'), blank = True , null = True, help_text='dd/mm/aaaa')
    cpf = models.CharField(_('CPF *'),max_length=14,help_text='ATENÇÃO: Somente os NÚMEROS')
    rg = models.CharField(_('RG *'),max_length=10,help_text='ATENÇÃO: Somente os NÚMEROS')
    matricula = models.CharField(_('Matrícula'),max_length=10,blank=True, null=True)
    lattes = models.CharField(_('Lattes *'), help_text="Clique <a href='http://buscatextual.cnpq.br/buscatextual' target='_blank'> aqui </a> para descobrir", max_length = 100)
    instituicao = models.ForeignKey('instituicao.Instituicao', verbose_name="Instituição", null=True, blank=True, on_delete=models.PROTECT)
    area_conhecimento_cnpq =  models.CharField(_('Área de conhecimento *'),max_length=50,choices=AREAS)
    curso_graduacao_vinculado = models.CharField(_('Curso de Graduação vinculado *'),help_text='Nome do curso que está lotado',max_length=50)
    curso_pos_graduacao = models.CharField(_('Curso de Pós-graduação vinculado'),null=True,blank=True,max_length=50,help_text='Caso esteja vinculado')
    grupo_pesquisa = models.CharField(_('Grupo de Pesquisa vinculado'),null=True,blank=True,max_length=100, help_text='Caso esteja vinculado')
    is_active = models.BooleanField(_('Ativo'), default=False, help_text='Se ativo, o usuário tem permissão para acessar o sistema')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    pc_artigos_qualis_a1_cinco_autores = models.IntegerField(_('Quantidade de artigos Qualis A1 até 5 autores'),blank=True,null=True, default=0)  #help_text='Minha ajuda para preencher o campo'
    pc_artigos_qualis_a1_mais_cinco_autores_primeiro_ultimo = models.IntegerField(_('Quantidade de artigos Qualis A1 com mais de 5 autores: Primeiro ou último ator'),blank=True, default=0)
    pc_artigos_qualis_a1_mais_cinco_autores_demais = models.IntegerField(_('Quantidade de artigos Qualis A1 com mais artigos até 5 autores: Demais posições de autoria'),blank=True, default=0)
    pc_artigos_qualis_a2_cinco_autores = models.IntegerField(_('Quantidade de artigos Qualis A2 até 5 autores'),blank=True, default=0)
    pc_artigos_qualis_a2_mais_cinco_autores_primeiro_ultimo = models.IntegerField(_('Quantidade de artigos Qualis A2 com mais de 5 autores: Primeiro ou último ator'),blank=True, default=0)
    pc_artigos_qualis_a2_mais_cinco_autores_demais = models.IntegerField(_('Quantidade de artigos Qualis A2 com mais artigos até 5 autores: Demais posições de autoria'),blank=True, default=0)
    pc_artigos_qualis_b1_b2_cinco_autores = models.IntegerField(_('Quantidade de artigos Qualis B1 e B2 até 5 autores'),blank=True, default=0)
    pc_artigos_qualis_b1_b2_mais_cinco_autores_primeiro_ultimo = models.IntegerField(_('Quantidade de artigos Qualis B1 e B2 com mais de 5 autores: Primeiro ou último ator'),blank=True, default=0)
    pc_artigos_qualis_b1_b2_mais_cinco_autores_demais = models.IntegerField(_('Quantidade de artigos Qualis B1 e B2 com mais artigos até 5 autores: Demais posições de autoria'),blank=True, default=0)
    pc_artigos_qualis_b3_b4_cinco_autores = models.IntegerField(_('Quantidade de artigos Qualis B3 e B4 até 5 autores'),blank=True, default=0)
    pc_artigos_qualis_b3_b4_mais_cinco_autores_primeiro_ultimo = models.IntegerField(_('Quantidade de artigos Qualis B3 e B4 com mais de 5 autores: Primeiro ou último ator'),blank=True, default=0)
    pc_artigos_qualis_b3_b4_mais_cinco_autores_demais = models.IntegerField(_('Quantidade de artigos Qualis B3 e B4 com mais artigos até 5 autores: Demais posições de autoria'),blank=True, default=0)
    pc_artigos_qualis_b5_c_cinco_autores = models.IntegerField(_('Quantidade de artigos Qualis B5 e C até 5 autores'),blank=True, default=0)
    pc_artigos_qualis_b5_c_mais_cinco_autores_primeiro_ultimo = models.IntegerField(_('Quantidade de artigos Qualis B3 e C com mais de 5 autores: Primeiro ou último ator'),blank=True, default=0)
    pc_artigos_qualis_b5_c_mais_cinco_autores_demais = models.IntegerField(_('Quantidade de artigos Qualis B3 e C com mais artigos até 5 autores: Demais posições de autoria'),blank=True, default=0)
    pc_trabalhos_anais_eventos = models.IntegerField(_('Quantidade de trabalhos completos em anais de eventos (LIMITE 10)'),validators=[MinValueValidator(0), MaxValueValidator(10)],blank=True, default=0)
    pc_resumos_anais_eventos = models.IntegerField(_('Quantidade de resumos ou resumos expandidos publicados em anais de eventos: (LIMITE 10):'),validators=[MinValueValidator(0), MaxValueValidator(10)],blank=True, default=0)
    pc_licenca_direito = models.IntegerField(_('Quantidade de licenças de direito de propriedade intelectual'),blank=True, default=0)
    pc_autoria_livros = models.IntegerField(_('Quantidade de autoria de Livros Técnico/Científico com ISBN publicados em editora que possua ou Comitê, ou Comissão ou Conselho Editorial'),blank=True, default=0)
    pc_autoria_livros_capitulos = models.IntegerField(_('Quantidade de capítulos e organização de Livros Técnico/Científico com ISBN publicados em editora que possua ou Comitê, ou Comissão ou Conselho Editorial'),blank=True, default=0)
    pc_orientador_teses_doutorado = models.IntegerField(_('Quantidade de teses de doutorado orientadas como orientador principal e aprovadas na UFN (LIMITE 5):'),validators=[MinValueValidator(0), MaxValueValidator(5)],blank=True, default=0)
    pc_orientador_mestrado = models.IntegerField(_('Quantidade de dissertações de mestrado orientadas como orientador principal e aprovadas na UFN (LIMITE 5):'),validators=[MinValueValidator(0), MaxValueValidator(5)],blank=True, default=0)
    pc_orientador_iniciacao_cientifica = models.IntegerField(_('Quantidade de orientações de Iniciação científica/Tecnológica na UFN em andamento ou concluída (LIMITE 6):'),validators=[MinValueValidator(0), MaxValueValidator(6)],blank=True, default=0)
    pc_orientador_trabalho_final_curso = models.IntegerField(_('Quantidade de orientações de Trabalho Final de Curso na UFN no estado concluído (LIMITE 6)'),validators=[MinValueValidator(0), MaxValueValidator(6)],blank=True, default=0)
    total_producoes = models.IntegerField(_('Total'), default = 0, blank=True, null=True)

    objects = UserManager()
    administradores = AdministradorAtivoManager()
    professores = ProfessorAtivoManager()
    bolsistas = BolsistaAtivoManager()
    bolsistas_inativos = BolsistaInativoManager()

    class Meta:
        ordering            =   [u'nome']
        verbose_name        =   _(u'usuário')
        verbose_name_plural =   _(u'usuários')

    def __str__(self):
        return self.nome

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_short_name(self):
        return self.nome[0:15].strip()

    def get_full_name(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.nome = self.nome.upper()
        if not self.id:
            self.set_password(self.password)
        super(Usuario, self).save(*args, **kwargs)

    def get_id(self):
        return self.id

    @property
    def is_staff(self):
        if self.tipo == 'ADMINISTRADOR':
            return True
        return False

    @property
    def get_absolute_url(self):
        return reverse('usuario_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('usuario_delete', args=[str(self.id)])

    @property
    def get_usuario_register_activate_url(self):
        return '%s%s' % (settings.DOMINIO_URL, reverse('usuario_register_activate', kwargs={'slug': self.slug}))

    @property
    def get_tres_anos_atras(self):
        agora = datetime.now()
        return agora.year - 3
        # - timedelta(days=3*365)
