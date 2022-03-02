from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Memory(models.Model):
    """Класс модели воспоминания пользователя"""

    title = models.CharField(
        max_length=256,
        verbose_name=_('Название'),
    )
    description = models.TextField(
        max_length=2048,
        verbose_name=_('Описание'),
        blank=True,
        null=True,
    )
    address = models.TextField(
        verbose_name=_('Адрес места'),
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='memories',
        related_query_name='memory',
        verbose_name=_('Пользователь'),
    )

    class Meta:
        """Класс настроек модели"""

        verbose_name = _('Воспоминание')
        verbose_name_plural = _('Воспоминания')

    def __str__(self) -> str:
        return str(self.title)
