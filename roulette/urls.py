from django.urls import path
from . import views as roulette_views

app_name = "roulette"

urlpatterns = [
    path("", roulette_views.mainpage, name="mainpage"),
    path("roulette/<int:menu_id>", roulette_views.menu_roulette, name="menu_roulette"),
]