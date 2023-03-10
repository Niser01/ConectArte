from django.urls import path
from apps.DM.views import *
app_name ="DM"

urlpatterns = [
    path("<str:username>", mensajes_privados),
    path("ms/<str:username>", DetailMs.as_view(), name="detailms"),
    path("inbox/", Inbox.as_view(), name="inbox"),
]
