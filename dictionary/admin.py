from django.contrib import admin
from .models import Dialect, Language

# class LanguageAdmin(admin.ModelAdmin):
# 	list_display = ['dialect', 'word']

admin.site.register(Dialect)
admin.site.register(Language)