from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(PreferenceTopic)
class PreferenceTopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'order')
    search_fields = ('name',)
    list_editable = ('order',)

@admin.register(PreferenceOption)
class PreferenceOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'order')
    list_filter = ('topic',)
    search_fields = ('name',)
    list_editable = ('order',)

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'option')
    list_filter = ('user', 'option__topic')