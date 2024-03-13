from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from dtapp.views import homePage, notFoundPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
]

handler404 = notFoundPage