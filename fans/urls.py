from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_fan, name='cadastro_fan'),
    path('cadastro/preferences/<int:fan_id>/', views.select_preferences, name='preferences'),
    path('cadastro/finalizado/', views.cadastro_finalizado, name='cadastro_finalizado'),
    path('vincular_perfil_esports/<int:fan_id>/', views.vincular_perfil_esports, name='vincular_perfil_esports'),
    path('instagram/', views.instagram_info_view, name='instagram_info'),
    path('twitter/', views.twitter_info_view, name='twitter_info'),
    path('', views.home, name='home'),
    path('perfil/<int:fan_id>/', views.profile_view, name='profile'),
    path('login/', views.login_email, name='login'),
    path('validar-perfil/', views.validar_perfil, name='validar_perfil'),
]
