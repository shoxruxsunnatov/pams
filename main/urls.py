from django.urls import path

from main.views import (
    HomeViewAPI
)

app_name = 'main'

urlpatterns = [
    path('', HomeViewAPI.as_view(), name='home_view_api')
]
