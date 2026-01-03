from django.urls import path

from . import views

urlpatterns: list = [
    # ex: /dlog/
    path("", views.index, name="index"), 
    path("form/", views.detail, name="detail"),
    path("results/", views.results, name="results"),
]