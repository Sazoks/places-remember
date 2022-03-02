from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class MemoryBoardView(LoginRequiredMixin, TemplateView):
    http_method_names = ('get', )
    template_name = 'memory_board/memory_board.html'
