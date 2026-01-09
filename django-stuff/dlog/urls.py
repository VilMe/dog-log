from django.urls import path

from . import views

app_name = "dlog"
urlpatterns: list = [
    # ex: /dlog/
    path("", views.index, name="index"), 
    # ex: /dlog/form
    path("form/", views.form, name="form"),
    path("results/", views.results, name="results"),
]