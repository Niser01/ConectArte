from django.urls import path 
from .views import *
app_name ="Usuarios"

urlpatterns = [
    path("<username>/",ProfileView.as_view(), name="perfil"),
    path("portfolio/<username>",PortfolioView.as_view(), name="portfolio"),
    path('profile/edit', EditProfile, name="editProfile"),

    #Se creó el nuevo path de followers, y de follow y unfollow
    path('profile/followers', followers, name="followers"),    
    path('follow/<str:username>/', follow, name="follow"),
    path('unfollow/<str:username>/', unfollow, name="unfollow"),
]