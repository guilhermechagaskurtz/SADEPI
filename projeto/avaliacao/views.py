from __future__ import unicode_literals

from django.contrib import messages
from django.http import Http404, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from utils.decorators import LoginRequiredMixin

from .models import Avaliacao
from .forms import AvaliacaoForm
from submissao.models import Submissao


class AvaliacaoListView(LoginRequiredMixin, ListView):
	model = Avaliacao

class AvaliacaoCreateView(LoginRequiredMixin, CreateView):
	model = Avaliacao
	form_class = AvaliacaoForm
	success_url = 'avaliacao_list'

	def get_initial(self):
		initials = super().get_initial()
		initials['submissao'] = Submissao.objects.get(id=self.request.GET.get('submissao_id'))
		return initials

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['submissao'] = Submissao.objects.get(id=self.request.GET.get('submissao_id'))
		return context

	def get_success_url(self):
		messages.success(self.request, 'Instância de avaliação criada com sucesso!!')
		return reverse(self.success_url)


class AvaliacaoUpdateView(LoginRequiredMixin, UpdateView):
	model = Avaliacao
	form_class = AvaliacaoForm
	success_url = 'avaliacao_list'
 
	def get_success_url(self):
		messages.success(self.request, 'Avaliação atualizada com sucesso!!')
		return reverse(self.success_url)


class AvaliacaoDeleteView(LoginRequiredMixin, DeleteView):
	model = Avaliacao
	success_url = 'avaliacao_list'

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()		
		success_url = self.get_success_url()
		try:
			self.object.delete()
			messages.success(request, 'Avaliação excluída com sucesso!') 
		except Exception as e:
			messages.error(request, 'Há dependências ligadas à essa avaliação, permissão negada!')
		return redirect(self.success_url)