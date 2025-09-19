from django.urls import path
from sala.api.views import CrearSalaCompletaAV, SalaDetailAV, ListarmySalas

urlpatterns = [
    
    path('', CrearSalaCompletaAV.as_view(), name="crear-sala"),
    path('showMysalas/', ListarmySalas.as_view(), name="crear-sala"),
    path('<int:id>', SalaDetailAV.as_view(), name="SPD-sala"),
    
    
    
]
