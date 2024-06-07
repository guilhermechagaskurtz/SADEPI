from django.conf.urls import url

from .views import (SubmissaoListView, SubmissaoCreateView,
					SubmissaoUpdateView, SubmissaoDeleteView,
					SubmissaoEditalListView, CarregaSelectProgramaAjaxView,
					RegraCampoEmpresaInstituicaoAjaxView)

urlpatterns = [
	url(r'edital/list/(?P<pk_edital>\d+)/(?P<situacao>[\w|\W]+)', SubmissaoEditalListView.as_view(), name='submissao_edital_list'),
	url(r'list/$', SubmissaoListView.as_view(), name='submissao_list'),
	url(r'cad/$', SubmissaoCreateView.as_view(), name='submissao_create'),
	url(r'ajax/carrega-select-programas/', CarregaSelectProgramaAjaxView.as_view(),
		name='ajax_carrega_select_programas'),
	url(r'ajax/regra-campo-empresa-instituicao/', RegraCampoEmpresaInstituicaoAjaxView.as_view(),
		name='ajax_regra_campo_empresa_instituicao'),
	url(r'(?P<pk>\d+)/$', SubmissaoUpdateView.as_view(), name='submissao_update'),
	url(r'(?P<pk>\d+)/delete/$', SubmissaoDeleteView.as_view(), name='submissao_delete'),
]
