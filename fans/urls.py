from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_fan, name='cadastro_fan'),
    path('cadastro/redes-sociais/<int:fan_id>/', views.cadastro_redes_sociais, name='cadastro_redes_sociais'),
    path('cadastro/finalizado/', views.cadastro_finalizado, name='cadastro_finalizado'),
    path('vincular_perfil_esports/<int:fan_id>/', views.vincular_perfil_esports, name='vincular_perfil_esports'),
    path('instagram/', views.instagram_info_view, name='instagram_info'),
    path('twitter/', views.twitter_info_view, name='twitter_info'),
    path('', views.home, name='home'),
]
