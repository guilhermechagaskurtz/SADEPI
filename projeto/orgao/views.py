from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from utils.decorators import LoginRequiredMixin

from .models import Orgao

class OrgaoListView(LoginRequiredMixin, ListView):
    model = Orgao


class OrgaoCreateView(LoginRequiredMixin, CreateView):
    model = Orgao
    fields = ['nome', 'sigla','site']
    success_url = 'orgao_list'
    

class OrgaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Orgao
    fields = ['nome', 'sigla','site']
    success_url = 'orgao_list'


class OrgaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Orgao
    success_url = 'orgao_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Órgão de fomento excluído com sucesso!') 
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse órgão de fomento, permissão negada!')
        return redirect(self.success_url)