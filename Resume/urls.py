from  django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("philani", views.philani, name="philani"),
    path("lungas", views.lungas, name="lungas")
]
