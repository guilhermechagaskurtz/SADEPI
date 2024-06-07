from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from utils.decorators import LoginRequiredMixin

from .models import Comissao
from datetime import datetime
from avaliacao.models import Avaliacao

class ComissaoListView(LoginRequiredMixin, ListView):
	model = Comissao


class ComissaoCreateView(LoginRequiredMixin, CreateView):
	model = Comissao
	template_name = 'comissao/comissao_form_create.html'
	fields = ['avaliacao_comissao']
	success_url = 'comissao_list'
	
	def get_initial(self):
		initials = super().get_initial()
		initials['avaliacao_comissao'] = Avaliacao.objects.get(id=self.request.GET.get('avaliacao_id'))
		return initials

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['avaliacao_comissao'] = Avaliacao.objects.get(id=self.request.GET.get('avaliacao_id'))
		return context

	def form_valid(self, form):
		comissao = form.save()
		comissao.dt_avaliacao_comissao = datetime.now()
		comissao.save()
		return super(ComissaoCreateView, self).form_valid(form)
	
	def get_success_url(self):
		messages.success(self.request, 'Instância de parecer criado com sucesso. Finalize-a assim que puder!')
		return reverse(self.success_url)

class ComissaoUpdateView(LoginRequiredMixin, UpdateView):
	model = Comissao
	fields = ['status', 'arquivo_parecer_comissao_final', 'comentario']
	success_url = 'comissao_list'
	
	def form_valid(self, form):
		comissao = form.save()
		comissao.dt_avaliacao_comissao = datetime.now()
		comissao.save()
		return super(ComissaoUpdateView, self).form_valid(form)
	
	def get_success_url(self):
		messages.success(self.request, 'Parecer atualizado com sucesso!')
		return reverse(self.success_url)

class ComissaoDeleteView(LoginRequiredMixin, DeleteView):
	model = Comissao
	success_url = 'comissao_list'
 
	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()		
		success_url = self.get_success_url()
		try:
			self.object.delete()
			messages.success(request, 'Parecer excluído com sucesso!') 
		except Exception as e:
			messages.error(request, 'Há dependências ligadas a esse parecer, permissão negada!')
		return redirect(self.success_url)