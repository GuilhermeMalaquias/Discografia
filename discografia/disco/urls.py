from django.urls import path, include
from django.conf import settings
from .views import musica_list, musica_new, musica_delete, musica_edit, relatorio

app_name = 'disco'

urlpatterns = [
    path('musica-list/', musica_list, name='musicalist'),
    path('musica_new/', musica_new, name='musica_new'),
    path('musica_delete/<int:pk>', musica_delete, name='musica_delete'),
    path('musica_edit/<int:pk>', musica_edit, name='musica_edit'),
    path('relatorio/', relatorio, name='relatorio'),
    ]

