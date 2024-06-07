from datetime import datetime

from django.contrib import messages
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, RedirectView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from avaliacao.models import Avaliacao

from programa.models import Programa

from submissao.models import Submissao

from utils.decorators import LoginRequiredMixin,  Professor_BolsistaRequiredMixin, ProfessorRequiredMixin

from usuario.models import Usuario

from .forms import MinhaAvaliacaoResponsavelForm, MinhaAvaliacaoSuplenteForm
from .forms import SubmissaoForm


class HomeView(LoginRequiredMixin, Professor_BolsistaRequiredMixin, TemplateView):
    template_name = 'appprofessor/home.html'

class AboutView(LoginRequiredMixin, TemplateView, Professor_BolsistaRequiredMixin):
    template_name = 'appprofessor/about.html'


class DadosProfessorUpdateView(LoginRequiredMixin, Professor_BolsistaRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'appprofessor/dados_professor_form.html'
    fields = ['nome', 'email','area_conhecimento_cnpq','curso_graduacao_vinculado','curso_pos_graduacao','grupo_pesquisa','data_nasc', 'cpf','rg','matricula', 'lattes', 'instituicao']
    success_url = 'appprofessor_home'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, 'Seus dados foram alterados com sucesso!')
        return reverse(self.success_url)


class ProducaoProfessorUpdateView(LoginRequiredMixin, ProfessorRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'appprofessor/producao_cientifica_form.html'
    fields = ['pc_artigos_qualis_a1_cinco_autores','pc_artigos_qualis_a1_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_a1_mais_cinco_autores_demais',
    'pc_artigos_qualis_a2_cinco_autores','pc_artigos_qualis_a2_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_a2_mais_cinco_autores_demais',
    'pc_artigos_qualis_b1_b2_cinco_autores','pc_artigos_qualis_b1_b2_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_b1_b2_mais_cinco_autores_demais',
    'pc_artigos_qualis_b3_b4_cinco_autores','pc_artigos_qualis_b3_b4_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_b3_b4_mais_cinco_autores_demais',
    'pc_artigos_qualis_b5_c_cinco_autores','pc_artigos_qualis_b5_c_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_b5_c_mais_cinco_autores_demais',
    'pc_trabalhos_anais_eventos','pc_resumos_anais_eventos','pc_licenca_direito','pc_autoria_livros','pc_autoria_livros_capitulos',
    'pc_orientador_teses_doutorado','pc_orientador_mestrado','pc_orientador_iniciacao_cientifica','pc_orientador_trabalho_final_curso','total_producoes']
    
    success_url = 'appprofessor_home'

    def get_object(self):
        return self.request.user

    def get_success_url(self): 
        messages.success(self.request, 'Seus dados de produção foram alterados com sucesso!')
        return reverse(self.success_url)


class ProducaoProfessorListView(LoginRequiredMixin, ProfessorRequiredMixin, ListView):
    model = Usuario 
    template_name = 'appprofessor/producao_cientifica_form.html'
    success_url = 'appprofessor_producao_list'


class SubmissaoListView(LoginRequiredMixin, ProfessorRequiredMixin, ListView):
    model = Submissao
    template_name = 'appprofessor/submissao_list.html'

    def get_queryset(self):
        queryset = super(SubmissaoListView, self).get_queryset()
        return queryset.filter(responsavel = self.request.user)
        

class SubmissaoCreateView(LoginRequiredMixin, ProfessorRequiredMixin, CreateView):
    model = Submissao
    template_name = 'appprofessor/submissao_form.html'
    form_class = SubmissaoForm
    success_url = 'appprofessor_submissao_list'

    def form_valid(self, form):
        try:
            # messages.warning(self.request, 'PASSEI')
            submissao = form.save(commit=False)
            submissao.responsavel = self.request.user
            submissao.save()
            self.object = submissao
        except Exception as e:
            messages.error(self.request, 'Erro ao submeter o projeto. %s' % e)
        
        return super(SubmissaoCreateView, self).form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Sua submissão foi gravada e enviada com sucesso!')
        return reverse(self.success_url)


class SubmissaoUpdateView(LoginRequiredMixin, ProfessorRequiredMixin, UpdateView):
    model = Submissao
    form_class = SubmissaoForm
    template_name = 'appprofessor/submissao_form.html'
    success_url = 'appprofessor_submissao_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Sua submissão foi alterada, gravada e enviada com sucesso!')
        return reverse(self.success_url)

class SubmissaoDeleteView(LoginRequiredMixin, ProfessorRequiredMixin, DeleteView):
    model = Submissao
    template_name = 'appprofessor/submissao_confirm_delete.html'
    success_url = 'appprofessor_submissao_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        # success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, 'Seu projeto foi removido da plataforma com sucesso!')
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à essa submissão, permissão negada!')
        return redirect(self.success_url)

    def get_success_url(self): 
        return reverse(self.success_url)


class CarregaSelectProgramaAjaxView(LoginRequiredMixin, View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        try:
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


class MinhaAvaliacaoListView(LoginRequiredMixin, ProfessorRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'appprofessor/minha_avaliacao_list.html'

    def get_queryset(self):
        queryset = super(MinhaAvaliacaoListView, self).get_queryset()
        return queryset.filter(Q(avaliador_responsavel = self.request.user) | Q(avaliador_suplente = self.request.user)) 
        


class MinhaAvaliacaoResponsavelUpdateView(LoginRequiredMixin, ProfessorRequiredMixin, UpdateView):
    model = Avaliacao
    form_class = MinhaAvaliacaoResponsavelForm
    template_name = 'appprofessor/minha_avaliacao_responsavel_form.html'
    success_url = 'appprofessor_minha_avaliacao_list'

    def get_object(self, queryset=None):
        """
        Não deixa entrar no formulário de avaliação se ele não foi designado como 
        avaliador responsável
        """
        pk = self.kwargs.get('pk')
        try:
            obj = Avaliacao.objects.get(pk=pk, avaliador_responsavel=self.request.user)
        except:
            raise Http404("Você não foi designado como avaliador responsável para esta submissão")
        return obj

    def form_valid(self, form):
        """
            Grava a data avaliação do responsável
        """
        avaliacao = form.save()
        avaliacao.dt_avaliacao_responsavel = datetime.now()
        print(avaliacao.dt_avaliacao_responsavel)
        avaliacao.save()
        return super(MinhaAvaliacaoResponsavelUpdateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Seu parecer como avaliador responsável foi enviado com sucesso!')
        return reverse(self.success_url)

class MinhaAvaliacaoSuplenteUpdateView(LoginRequiredMixin, ProfessorRequiredMixin, UpdateView):
    model = Avaliacao
    form_class = MinhaAvaliacaoSuplenteForm
    template_name = 'appprofessor/minha_avaliacao_suplente_form.html'
    success_url = 'appprofessor_minha_avaliacao_list'

    def get_object(self, queryset=None):
        """
        Não deixa entrar no formulário de avaliação se ele não foi designado como 
        avaliador suplente
        """
        pk = self.kwargs.get('pk')
        try:
            obj = Avaliacao.objects.get(pk=pk, avaliador_suplente=self.request.user)
        except:
            raise Http404("Você não foi designado como avaliador suplente para esta submissão")
        return obj

    def form_valid(self, form):
        """
            Grava a data avaliação do suplente
        """
        avaliacao = form.save()
        avaliacao.dt_avaliacao_suplente = datetime.now()
        avaliacao.save()
        return super(MinhaAvaliacaoSuplenteUpdateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Seu parecer como avaliador suplente foi enviado com sucesso!')
        return reverse(self.success_url)