from django.urls.conf import path

from .views import view_b
from .views import view_c
from .views import api_materie


app_name="prova_pratica"

urlpatterns = [
    path("view_b",view_b,name="view_b"),
    path("view_c",view_c,name="view_c"),
    path("api_materie",api_materie,name="api_materie"),
]