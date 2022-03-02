import logging
import requests
from django.core.files.base import ContentFile

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

    if backend.name == 'facebook':
        avatar_url = \
            'https://graph.facebook.com/{}/picture?type=large' \
            .format(response['id'])
    elif backend.name == 'vk-oauth2':
        avatar_url = response['photo']
    else:
        avatar_url = None

    if avatar_url and is_new:
        try:
            avatar_resp = requests.get(avatar_url, params={'type': 'large'})
            avatar_resp.raise_for_status()
        except requests.HTTPError as error:
            logging.error(error)
        else:
            avatar_file = ContentFile(avatar_resp.content)
            full_name = response['first_name'] + ' ' + response['last_name']

            print(avatar_file, type(avatar_file))
            print(avatar_url, type(avatar_url))
            # new_profile = Profile(user=user)
            # new_profile.avatar.save
            # new_profile.save()
            #
            # user.avatar.save(f'{user.id}.jpg', avatar_file)
            # user.full_name = full_name
            # user.save(update_fields=['avatar', 'full_name'])