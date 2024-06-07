from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin

from usuario.models import Usuario


class HomeRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        if self.request.user.tipo == 'ADMINISTRADOR':
            return reverse('home')
        elif self.request.user.tipo == 'PROFESSOR':
            return reverse('appprofessor_home')
        elif self.request.user.tipo == 'BOLSISTA':
            return reverse('appprofessor_home')


class HomeView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'core/home.html'


class AboutView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'core/about.html'
