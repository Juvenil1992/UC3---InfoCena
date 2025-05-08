

from django.urls import path

from Site import views


urlpatterns = [
    path('', views.index, name = 'index')
]