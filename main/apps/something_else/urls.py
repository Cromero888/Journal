from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^add/', views.addstrain),
    url(r'^journal/', views.journal),
    url(r'^$', views.index),
]