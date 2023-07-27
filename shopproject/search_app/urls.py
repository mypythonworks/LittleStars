from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from search_app import views

app_name='search_app'

urlpatterns = [
    path('', views.searchResult, name='searchResult'),
]
