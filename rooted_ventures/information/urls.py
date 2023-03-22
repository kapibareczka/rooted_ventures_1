from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="information_home"),
    path("contact", views.contact, name="contact"),
]
