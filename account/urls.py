from django.urls import path, include

from . import views as v


urlpatterns = [
    path('dashboard/', v.index, name='index'),
    path('account/', include('django.contrib.auth.urls')),
]
