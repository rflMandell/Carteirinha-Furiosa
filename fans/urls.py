from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_fan, name='cadastro_fan'),
    path('cadastro/redes-sociais/<int:fan_id>/', views.cadastro_redes_sociais, name='cadastro_redes_sociais'),
    path('cadastro/finalizado/', views.cadastro_finalizado, name='cadastro_finalizado'),
]
