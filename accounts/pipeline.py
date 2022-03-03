import wget
import logging
import requests
from django.core.files.base import ContentFile
from places_remember.settings import BASE_DIR

from .models import Profile


def get_profile_image(backend, user, response, is_new=False, *args, **kwargs):
    """
    Функция для получения аватара профиля пользователя.

    :param backend: Используемый бэкенд аутентификации.
    :param user: Текущий пользователь.
    :param response: Объект ответа.
    :param is_new: Флаг нового пользователя.
    :param args: Неименованные параметры запроса.
    :param kwargs: Именованные параметры запроса.
    """

    if user is None:
        return

    avatar_url = None

    if backend.name == 'vk-oauth2':
        avatar_url = response['photo']

    if avatar_url and is_new:
        print(avatar_url)
        new_profile = Profile(avatar=avatar_url, user=user)
        new_profile.save()
