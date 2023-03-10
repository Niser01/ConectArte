from django.urls import path 
from .views import VacanteView
app_name ="vacantes"

urlpatterns = [
    path("MostrarVacantes/",VacanteView.as_view(), name="vacante"),
    
]
## URLS DE VACANTES