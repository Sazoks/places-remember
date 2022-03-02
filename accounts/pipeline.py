from .models import Profile


# FIXME: Сделать нормальную загрузку аватара.
def get_avatar(backend, response, user=None, *args, **kwargs):
    """
    Функция для получения автара пользователя из соц. сети и
    сохранения ее в связанной с моделью User модели Profile.

    :param backend: Используемый бэкенд аутентификации.
    :param response: Объект ответа.
    :param user: Пользователь.
    :param args: Неименованные параметры запроса.
    :param kwargs: Именованные параметры запроса.
    """

    url = None

    if backend.name == 'vk-oauth2':
        url = response.get('photo', '')

    if url and user:
        if not Profile.objects.filter(user__pk=user.pk).first():
            new_profile = Profile(avatar=url, user=user)
            new_profile.save()
        else:
            user.profile.avatar = url
            user.profile.save()
