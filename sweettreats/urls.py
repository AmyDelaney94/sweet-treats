'''
    Documenting imports at beginning of file
'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='posts'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='posts_like'),
    path('create_posts', views.createposts, name='create_posts'),
]
