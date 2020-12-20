from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ginger", views.ginger, name="ginger"),
    path("gayis", views.gayis, name="gayis"),
    path("<str:name>", views.greet, name="greet")
]