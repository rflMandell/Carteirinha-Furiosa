from django.contrib import admin
from .models import Fan, PreferenceTopic, PreferenceOption, UserPreference

admin.site.register(Fan)
admin.site.register(PreferenceTopic)
admin.site.register(PreferenceOption)
admin.site.register(UserPreference)