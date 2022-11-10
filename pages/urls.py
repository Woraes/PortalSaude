from django.urls import path
from .views import Home, Manutencao, Sistemas, Esf, Manutencao, Ubs, UbsBrisamar, Secretaria, TeleMedicina, Hmsfx, Cpd
from .views import UbsCentro, UbsChaperoA, UbsEngenho, UbsMangueira, UbsCalifornia, UbsVilaGeny, UbsVilaMargarida, UbsVistaAlegre, Especialidades
from .views import EsfPiranema, EsfOdenit, EsfChaperob, EsfCoroa, EsfSanta, EsfIlhaDaMadeira, EsfJardim, EsfMazomba, EsfSaco
from .views import Sistema
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('sistemas/', Sistemas.as_view(), name='sistemas'),
    path('secretaria/', Secretaria.as_view(), name='secretaria'),
    path('hmsfx/', Hmsfx.as_view(), name='hmsfx'),
    path('esf/', Esf.as_view(), name='esf'),
    path('ubs/', Ubs.as_view(), name='ubs'),
    path('especialidades/', Especialidades.as_view(), name='especialidades'),
    path('telemedicina/', TeleMedicina.as_view(), name='telemedicina'),
    path('manutencao/', Manutencao.as_view(), name='manutencao'),
    path('ubsbrisamar/', UbsBrisamar.as_view(), name='ubsbrisamar'),
    path('ubscentro/', UbsCentro.as_view(), name='ubscentro'),
    path('ubschaperoa/', UbsChaperoA.as_view(), name='ubschaperoa'),
    path('ubsengenho/', UbsEngenho.as_view(), name='ubsengenho'),
    path('ubsmangueira/', UbsMangueira.as_view(), name='ubsmangueira'),
    path('ubscalifornia/', UbsCalifornia.as_view(), name='ubscalifornia'),
    path('ubsvilageny/', UbsVilaGeny.as_view(), name='ubsvilageny'),
    path('ubsvilamargarida/', UbsVilaMargarida.as_view(), name='ubsvilamargarida'),
    path('ubsvistaalegre/', UbsVistaAlegre.as_view(), name='ubsvistaalegre'),
    path('esfpiranema/', EsfPiranema.as_view(), name='esfpiranema'),
    path('esfodenit/', EsfOdenit.as_view(), name='esfodenit'),
    path('esfchaperob/', EsfChaperob.as_view(), name='esfchaperob'),
    path('esfcoroa/', EsfCoroa.as_view(), name='esfcoroa'),
    path('esfsanta/', EsfSanta.as_view(), name='esfsanta'),
    path('esfilha/', EsfIlhaDaMadeira.as_view(), name='esfilha'),
    path('esfjardim/', EsfJardim.as_view(), name='esfjardim'),
    path('esfmazomba/', EsfMazomba.as_view(), name='esfmazomba'),
    path('esfsaco/', EsfSaco.as_view(), name='esfsaco'),
    path('cpd/', Cpd.as_view(), name='cpd'),
    path('teste/', Sistema , name='teste'),
    
]
