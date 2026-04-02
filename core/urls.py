from django.contrib import admin
from django.urls import path

from client.views import BasePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BasePage.as_view(), name='base_page')
]
