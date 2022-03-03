from typing import (
    Dict,
    Any,
)

from django.urls import reverse_lazy
from django.http import (
    HttpResponse,
    HttpRequest,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import ModelFormMixin
from django.views.generic.list import ListView
from django.db.models import QuerySet

from .forms import MemoryForm


class CreateAndListMemoriesView(LoginRequiredMixin,
                                ModelFormMixin,
                                ListView):
    """
    Класс-контроллер для вывода списка воспоминаний пользователя
    и сохранения нового воспоминания через форму.
    """

    http_method_names = ('get', 'post')
    template_name = 'memory_board/memory_board.html'
    form_class = MemoryForm
    success_url = reverse_lazy('memory_board:list_or_create')
    object = None

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        """Метод генерации контекста шаблона"""

        # Удобочитаемый memories вместо абстрактного object_list.
        context = {
            'memories': self.get_queryset(),
        }
        return super().get_context_data(**context, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Метод добавления нового воспоминания"""

        self.object_list = self.get_queryset()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_queryset(self) -> QuerySet:
        """
        Метод получения списка воспоминаний текущего пользователя.

        :return: Список всех воспоминаний текущего пользователя.
        """

        return self.request.user.memories.all()

    def form_valid(self, form) -> HttpResponse:
        """Метод валидации формы"""

        # Связываем воспоминание с текущим юзером.
        new_memory = form.save(commit=False)
        new_memory.user = self.request.user

        return super().form_valid(form)
