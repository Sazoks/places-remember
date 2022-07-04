from django.contrib.auth import get_user_model


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

    UserModel = get_user_model()

    if user is None:
        return

    avatar_url = None

    if backend.name == 'vk-oauth2':
        avatar_url = response['photo']

    if avatar_url and is_new:
        new_profile = UserModel(avatar=avatar_url)
        new_profile.save()
