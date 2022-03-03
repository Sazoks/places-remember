"""places_remember URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (
    path,
    include,
)
from django.conf.urls.static import (
    static,
    settings,
)
from django.views.generic.base import RedirectView


admin.autodiscover()

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='memory_board:list_or_create',
                                  permanent=True)),
    path('memory-board/', include('memory_board.urls')),
    path('accounts/', include('accounts.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document=settings.MEDIA_ROOT)
