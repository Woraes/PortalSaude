
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .form import UsuarioForm
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DeleteView
from .models import Perfil, User
import os
import platform












class UsuarioList(GroupRequiredMixin ,LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u'ADM'
    model = Perfil
    template_name = 'usuariolist.html'
    
  



class UsuarioNew(GroupRequiredMixin ,LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'ADM'

    template_name = 'form.html'
    # model = User
    # fields = ['username', 'email', 'password','groups' ]
    form_class = UsuarioForm
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        
        
        # Como aqui vem os dados do forms.py, não temos o form.instance e sim o form.cleaned_data
        # pegamos o nome do grupo que o usuário marcou no select e buscamos o objeto só para garantir 
        grupo = get_object_or_404(Group, name=form.cleaned_data['grupo'].name)        
        
        
         # Aqui cria o usuário no banco
        url = super().form_valid(form)
        # Adiciona o grupo ao objeto usuário e salva
        self.object.groups.add(grupo)
        self.object.save()
        
        Perfil.objects.create(usuario=self.object)
        
        
        return url


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = 'Criar Usuário'
        context['botao'] = 'Salvar'
        context['descri'] = 'Bem Vindo Crie o Usuário'
        context['sair'] = 'sair'
        
        return context
    
    
class UsuarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'ADM',
    model = Perfil
    fields = ['nome',
              'cpf',
              'telefone',
              'email',
              'cep',
              ]
    template_name = 'form.html'
    success_url = reverse_lazy('adminlist')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object
    
    
        

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = 'Editar Usuario'
        context['botao'] = 'Salvar'
        context['descri'] = 'Complete seu cadastro'
        
        return context
    
    
class UsuarioDados(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'ADM',
    model = Perfil
    fields = ['nome',
              'cpf',
              'telefone',
              'email',
              'cep',
              ]
    template_name = 'form.html'
    success_url = reverse_lazy('adminlist')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object
    
    
        

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = 'Cadastro'
        context['botao'] = 'Salvar'
        context['descri'] = 'Complete seu cadastro'
        
        return context
    
 
class UsuarioDelete(GroupRequiredMixin ,LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'ADM'
    model = Perfil
    template_name = 'usuariodelete.html'
    success_url = reverse_lazy('adminlist')
    
    # def get_object(self, queryset=None):
    #     self.object = get_object_or_404(Perfil, pk=self.kwargs['pk'], criadopor=self.request.user) 
    #     return self.object      

class PainelAdm(GroupRequiredMixin ,LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    group_required = u'ADM'

    template_name = ''
    
    


class PortalSaude(TemplateView):
     template_name ='painel.html'   
     

class Registrar(TemplateView):
    
    template_name = 'registrar.html'     
    