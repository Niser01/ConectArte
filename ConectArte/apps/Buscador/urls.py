from django.urls import path 
from .views import SearchArtist
app_name ="Buscador"

urlpatterns = [
    path("search/",SearchArtist.as_view(), name="searchProfile"),
]