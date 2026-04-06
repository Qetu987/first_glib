from django.contrib import admin
from django.urls import path

from client.views import IndexPage, SubPagePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPage.as_view(), name='index_page'),
    path('index/', SubPagePage.as_view(), name='sub_page_page'),
]
