from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView


class UserLoginView(TemplateView):
    """
    Класс-контроллер для авторизации пользователей.

    Т.к. используется только авторизация через соц. сети,
    нужда в форме аутентификации пропадает.
    """

    http_method_names = ('get', )
    template_name = 'accounts/login.html'


class UserLogoutView(LogoutView):
    """Класс-контроллер выхода из системы"""

    http_method_names = ('get', )
    template_name = 'accounts/logout.html'
    next_page = 'accounts:login'
