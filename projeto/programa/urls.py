from django.conf.urls import url

from .views import (ProgramaListView, ProgramaCreateView,
					ProgramaUpdateView, ProgramaDeleteView)


urlpatterns = [
	url(r'list/$', ProgramaListView.as_view(), name='programa_list'),
	url(r'cad/$', ProgramaCreateView.as_view(), name='programa_create'),
	url(r'(?P<pk>\d+)/$', ProgramaUpdateView.as_view(), name='programa_update'),
	url(r'(?P<pk>\d+)/delete/$', ProgramaDeleteView.as_view(), name='programa_delete'),
]
