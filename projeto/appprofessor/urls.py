from django.conf.urls import url

from core.views import HomeRedirectView

from .views import (ProducaoProfessorListView, ProducaoProfessorUpdateView, SubmissaoListView,SubmissaoUpdateView,
                    SubmissaoCreateView,SubmissaoDeleteView,
                    MinhaAvaliacaoListView,
                    HomeView, AboutView, MinhaAvaliacaoResponsavelUpdateView,
                    MinhaAvaliacaoSuplenteUpdateView,DadosProfessorUpdateView,CarregaSelectProgramaAjaxView,
					     RegraCampoEmpresaInstituicaoAjaxView)

urlpatterns = [
   url(r'^home$', HomeView.as_view(), name='appprofessor_home'), 
   url(r'^$', HomeRedirectView.as_view(), name='home_redirect'),
   url(r'^about$', AboutView.as_view(), name='appprofessor_about'),
   
   url(r'^meus-dados/', DadosProfessorUpdateView.as_view(), name='appprofessor_dados_update'),
   url(r'^minhas-producoes/', ProducaoProfessorUpdateView.as_view(), name='appprofessor_producao_update'),
   url(r'^minhas-producoes/cad/(?P<pk>\d+)/$', ProducaoProfessorListView.as_view(), name='appprofessor_producao_list'),
   
   url(r'^minhas-submissoes/(?P<pk>\d+)/$', SubmissaoUpdateView.as_view(), name='appprofessor_submissao_update'),
   url(r'^minhas-submissoes$', SubmissaoListView.as_view(), name='appprofessor_submissao_list'),
   url(r'^minhas-submissoes/cad$', SubmissaoCreateView.as_view(), name='appprofessor_submissao_create'),
   url(r'(?P<pk>\d+)/delete/$', SubmissaoDeleteView.as_view(), name='appprofessor_submissao_delete'),
   url(r'^minhas-avaliacoes$', MinhaAvaliacaoListView.as_view(), name='appprofessor_minha_avaliacao_list'),
   url(r'^minhas-avaliacoes/avaliacao/(?P<pk>\d+)/responsavel/$', MinhaAvaliacaoResponsavelUpdateView.as_view(), name='appprofessor_minha_avaliacao_responsavel'),
   url(r'^minhas-avaliacoes/avaliacao/(?P<pk>\d+)/suplente/$', MinhaAvaliacaoSuplenteUpdateView.as_view(), name='appprofessor_minha_avaliacao_suplente'),
]
