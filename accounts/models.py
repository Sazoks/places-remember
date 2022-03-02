from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """Модель профиля для расширения модели User"""

    avatar = models.ImageField(
        upload_to='user_avatars',
        verbose_name=_('Аватар пользователя'),
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='profile',
        related_query_name='profile',
        verbose_name=_('Пользователь'),
    )

    class Meta:
        """Класс настроек модели"""

        verbose_name = _('Профиль')
        verbose_name_plural = _('Профили')

    def __str__(self) -> str:
        return f'{self.user.username} profile'
