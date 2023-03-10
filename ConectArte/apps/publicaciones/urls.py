from django.urls import path 
from .views import commentView

app_name ="publicaciones"
urlpatterns = [ 
    path('publicacion/<int:pk>/', commentView.as_view(), name="comments"),
]