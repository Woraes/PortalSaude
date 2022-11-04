from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioNew, PainelAdm, UsuarioList, PerfilUpdate, PortalSaude, Registrar





urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name = 'login.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name = 'logout.html'
        ), name='logout'),
    path('registro/', UsuarioNew.as_view(), name='registro'),
    path('admin/', PainelAdm.as_view(), name='paineladm'),
    path('adminlist/', UsuarioList.as_view(), name='adminlist'),
    path('perfilupdate/',  PerfilUpdate.as_view(), name='perfilupdate'),
    path('portal/', PortalSaude.as_view(), name='portal_saude'),
    path('registrar/', Registrar.as_view(), name='registrar'),   
    
    
    
]





