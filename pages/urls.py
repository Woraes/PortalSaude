from django.urls import path
from .views import Home, Manutencao, Sistemas, Esf, Manutencao, Ubs, UbsBrisamar, Secretaria, TeleMedicina, Hmsfx, Cpd
from .views import UbsCentro, UbsChaperoA, UbsEngenho


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('sistemas/', Sistemas.as_view(), name='sistemas'),
    path('secretaria/', Secretaria.as_view(), name='secretaria'),
    path('hmsfx/', Hmsfx.as_view(), name='hmsfx'),
    path('esf/', Esf.as_view(), name='esf'),
    path('ubs/', Ubs.as_view(), name='ubs'),
    path('telemedicina/', TeleMedicina.as_view(), name='telemedicina'),
    path('manutencao/', Manutencao.as_view(), name='manutencao'),
    path('ubsbrisamar/', UbsBrisamar.as_view(), name='ubsbrisamar'),
    path('ubscentro/', UbsCentro.as_view(), name='ubscentro'),
    path('ubschaperoa/', UbsChaperoA.as_view(), name='ubschaperoa'),
    path('ubsengenho/', UbsEngenho.as_view(), name='ubsengenho'),
    path('cpd/', Cpd.as_view(), name='cpd'),
]
