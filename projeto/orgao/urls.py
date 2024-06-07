from django.conf.urls import url

from .views import OrgaoListView, OrgaoCreateView
from .views import OrgaoUpdateView, OrgaoDeleteView


urlpatterns = [
	url(r'list/$', OrgaoListView.as_view(), name='orgao_list'),
	url(r'cad/$', OrgaoCreateView.as_view(), name='orgao_create'),
	url(r'(?P<pk>\d+)/$', OrgaoUpdateView.as_view(), name='orgao_update'),
	url(r'(?P<pk>\d+)/delete/$', OrgaoDeleteView.as_view(), name='orgao_delete'),
]
