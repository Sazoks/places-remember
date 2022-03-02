from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MemoryBoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'memory_board'
    verbose_name = _('Доска воспоминаний')
