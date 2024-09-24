from django.contrib import admin

# Register your models here.
from .models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass
