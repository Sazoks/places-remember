from django.urls import  path

from . import views

app_name = 'memory_board'
urlpatterns = [
    path('', views.CreateAndListMemoriesView.as_view(), name='list_or_create'),
]
