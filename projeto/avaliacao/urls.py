from django.conf.urls import url

from .views import AvaliacaoListView, AvaliacaoCreateView
from .views import AvaliacaoUpdateView, AvaliacaoDeleteView


urlpatterns = [
	url(r'list/$', AvaliacaoListView.as_view(), name='avaliacao_list'),
	url(r'cad/$', AvaliacaoCreateView.as_view(), name='avaliacao_create'),
	url(r'(?P<pk>\d+)/$', AvaliacaoUpdateView.as_view(), name='avaliacao_update'),
	url(r'(?P<pk>\d+)/delete/$', AvaliacaoDeleteView.as_view(), name='avaliacao_delete'),
]
