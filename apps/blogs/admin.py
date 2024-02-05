from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ("id", "title")
    list_display_links = ("id",)
