from django.contrib import admin
from django import forms
from .models import MindMap
# Register your models here.

class MindMapAdmin(admin.ModelAdmin):
    list_display = ('big_label', 'small_label', 'contents')

admin.site.register(MindMap, MindMapAdmin)


