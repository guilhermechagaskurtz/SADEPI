from __future__ import unicode_literals

from django.contrib import messages
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from utils.decorators import LoginRequiredMixin

from edital.models import Edital
from programa.models import Programa

from .models import Submissao
from .forms import SubmissaoForm

class SubmissaoListView(LoginRequiredMixin, ListView):
    model = Submissao


class SubmissaoCreateView(LoginRequiredMixin, CreateView):
    model = Submissao
    form_class = SubmissaoForm
    success_url = 'submissao_list'


class SubmissaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Submissao
    form_class = SubmissaoForm
    success_url = 'submissao_list'


class SubmissaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Submissao
    success_url = 'submissao_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Submissão excluída com sucesso!') 
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à essa submissão, permissão negada!')
        return redirect(self.success_url)


class SubmissaoEditalListView(LoginRequiredMixin, ListView):
    model = Submissao
    template_name = 'submissao/submissao_edital_list.html'

    def get_queryset(self):
        edital = Edital.objects.get(id=self.kwargs.get('pk_edital'))
        situacao = self.kwargs.get('situacao')
        # print(situacao)
        if situacao == 'APROVADAS':
            return edital.submissoes_aprovadas
        elif situacao == 'REPROVADAS':
            return edital.submissoes_reprovadas
        elif situacao == 'TODAS':
            return edital.submissoes

    def get_context_data(self):
        context = super().get_context_data()
        context['edital'] = Edital.objects.get(pk=self.kwargs['pk_edital'])
        context['situacao'] = self.kwargs.get('situacao')
        return context


class CarregaSelectProgramaAjaxView(LoginRequiredMixin, View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        try:
            # print("passando ........")
            edital_id  = self.request.POST.get('edital_id')
            edital = Edital.objects.get(id=edital_id)

            programas_edital_lista = [{'id':'', 'sigla':'---------'}]
            for programa in edital.programa.all():
                programas_edital_lista.append({'id':programa.id, 'sigla':programa.sigla})

            return JsonResponse(data={'programas':programas_edital_lista, 'obriga_bolsista': edital.bolsista})
        except Exception as e:
            mensagem_erro = 'Erro ao carregar os programas para o edital. Erro: %s' % str(e)
            return JsonResponse(data={'erro': mensagem_erro}, status=400)


class RegraCampoEmpresaInstituicaoAjaxView(LoginRequiredMixin, View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        try:
            programa_id  = self.request.POST.get('programa_id')
            programa = Programa.objects.get(id=programa_id)

            return JsonResponse(data={'obriga_empresa': programa.tem_empresa_parceira, 'obriga_instituicao': programa.tem_instituicao_beneficiada})
        except Exception as e:
            mensagem_erro = 'Erro ao mostrar/esconder os campos Empresa e Instituição. Erro: %s' % str(e)
            return JsonResponse(data={'erro': mensagem_erro}, status=400)