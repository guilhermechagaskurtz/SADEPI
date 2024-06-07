from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse

from django.views.generic import ListView,TemplateView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from mail_templated import EmailMessage

from utils.decorators import LoginRequiredMixin

from .models import Usuario
from .forms import UsuarioRegisterForm


class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario


class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ['tipo', 'nome', 'email','area_conhecimento_cnpq','curso_graduacao_vinculado','curso_pos_graduacao','grupo_pesquisa','data_nasc', 'cpf','rg' ,'matricula', 'lattes', 'instituicao', 'password', 'is_active']
    success_url = 'usuario_list'


class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['tipo', 'nome', 'email','area_conhecimento_cnpq','curso_graduacao_vinculado','curso_pos_graduacao','grupo_pesquisa','data_nasc', 'cpf','rg','matricula', 'lattes', 'instituicao', 'is_active',
    'pc_artigos_qualis_a1_cinco_autores','pc_artigos_qualis_a1_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_a1_mais_cinco_autores_demais',
    'pc_artigos_qualis_a2_cinco_autores','pc_artigos_qualis_a2_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_a2_mais_cinco_autores_demais',
    'pc_artigos_qualis_b1_b2_cinco_autores','pc_artigos_qualis_b1_b2_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_b1_b2_mais_cinco_autores_demais',
    'pc_artigos_qualis_b3_b4_cinco_autores','pc_artigos_qualis_b3_b4_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_b3_b4_mais_cinco_autores_demais',
    'pc_artigos_qualis_b5_c_cinco_autores','pc_artigos_qualis_b5_c_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_b5_c_mais_cinco_autores_demais',
    'pc_trabalhos_anais_eventos','pc_resumos_anais_eventos','pc_licenca_direito','pc_autoria_livros','pc_autoria_livros_capitulos',
    'pc_orientador_teses_doutorado','pc_orientador_mestrado','pc_orientador_iniciacao_cientifica','pc_orientador_trabalho_final_curso','total_producoes']
    template_name = 'usuario/usuario_form_update.html'
    success_url = 'usuario_list'


class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = 'usuario_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Usuário excluído com sucesso!') 
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse usuário, permissão negada!')
        return redirect(self.success_url)


class UsuarioRegisterView(CreateView):
    model = Usuario
    form_class = UsuarioRegisterForm
    template_name = 'usuario/usuario_register_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UsuarioRegisterView, self).form_valid(form)
    
    def get_success_url(self):
        message = EmailMessage('usuario/email/validacao_email.html', {'usuario': self.object},
                               settings.EMAIL_HOST_USER, to=[self.object.email])
        message.send()     
        return reverse('usuario_register_success')


class UsuarioRegisterSuccessView(TemplateView):
    template_name= 'usuario/usuario_register_success.html'


class UsuarioRegisterActivateView(RedirectView):
    models = Usuario

    def get_redirect_url(self, *args, **kwargs):
        self.object = Usuario.objects.get(slug=kwargs.get('slug'))
        self.object.is_active = True
        self.object.save()
        login(self.request, self.object)
        messages.success(self.request, 'Obrigado por acessar o SISGEP/COMIC. Esta é a sua área restrita de submissão, avaliação e acompanhamento de projetos.')
        return reverse('appprofessor_home')