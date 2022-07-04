from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Модель пользователя.

    В переопределенной модели пользователя добавили
    поле для автара.
    """

    avatar = models.URLField(
        null=True,
        blank=True,
        verbose_name=_('Ссылка на аватар'),
    )
