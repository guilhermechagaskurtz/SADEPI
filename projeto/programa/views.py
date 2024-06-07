from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from utils.decorators import LoginRequiredMixin

from .models import Programa


class ProgramaListView(LoginRequiredMixin, ListView):
    model = Programa


class ProgramaCreateView(LoginRequiredMixin, CreateView):
    model = Programa
    fields = ['nome', 'sigla', 'tem_empresa_parceira', 'tem_instituicao_beneficiada']
    success_url = 'programa_list'


class ProgramaUpdateView(LoginRequiredMixin, UpdateView):
    model = Programa
    fields = fields = ['nome', 'sigla', 'tem_empresa_parceira', 'tem_instituicao_beneficiada']
    success_url = 'programa_list'


class ProgramaDeleteView(LoginRequiredMixin, DeleteView):
    model = Programa
    success_url = 'programa_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Programa institucional excluído com sucesso!') 
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse programa, permissão negada!')
        return redirect(self.success_url)