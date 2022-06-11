'''
    Documenting imports at beginning of file
'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home')
]
