from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class Home(TemplateView):
    template_name = 'index.html'
    
    
class Sistemas(TemplateView):
    template_name = 'sistemas.html' 
    
    
class Secretaria(TemplateView):
    template_name = 'secretaria.html'
    
    
class Hmsfx(TemplateView):
    template_name = 'hmsfx.html'              
    

class Esf(TemplateView):
    template_name = 'esf.html'  
    

class Ubs(TemplateView):
    template_name = 'ubs.html'      
    

class Manutencao(TemplateView):
    template_name = 'manutencao.html'
    
class Especialidades(TemplateView):
    template_name = 'especialidades.html'       
    
    
    
class UbsBrisamar(TemplateView):
    template_name = 'ubsbrisamar.html'  
    
class UbsCentro(TemplateView):
    template_name = 'ubscentro.html' 
    
class UbsChaperoA(TemplateView):
    template_name = 'ubschaperoa.html'
    
class UbsEngenho(TemplateView):
    template_name = 'ubsengenho.html' 

class UbsMangueira(TemplateView):
    template_name = 'ubsmangueira.html' 

class UbsCalifornia(TemplateView):
    template_name = 'ubscalifornia.html'
    
class UbsVilaGeny(TemplateView):
    template_name = 'ubsvilageny.html'                                 
  



class EsfPiranema(TemplateView):
    template_name = 'esfpiranema.html' 
    
class EsfOdenit(TemplateView):
    template_name = 'esfodenit.html' 
    
class EsfChaperob(TemplateView):
    template_name = 'esfchaperob.html'

class EsfCoroa(TemplateView):
    template_name = 'esfcoroa.html'  

class EsfSanta(TemplateView):
    template_name = 'esfsanta.html'                    
    
    
    
    

class TeleMedicina(TemplateView):
    template_name = 'telemedicina.html'
    
    
      
    
 
   
class Cpd( LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'cpd.html'     
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['unidade'] = 'Cpd Saúde'
        context['botao'] = 'Salvar'
        context['descri'] = 'Complete seu cadastro'
        
        return context     