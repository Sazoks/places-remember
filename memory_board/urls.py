from django.urls import  path

from .views import MemoryBoardView

app_name = 'memory_board'
urlpatterns = [
    path('', MemoryBoardView.as_view(), name='my_memories'),
]
