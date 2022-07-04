from django.contrib import admin

from . import models


@admin.register(models.Memory)
class MemoryAdmin(admin.ModelAdmin):
    """Класс настроек админки для модели воспоминаний"""

    list_display = ('title', 'description', 'address')
    list_display_links = ('title', )
