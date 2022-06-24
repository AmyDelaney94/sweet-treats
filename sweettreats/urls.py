'''
    Documenting imports at beginning of file
'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='posts'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='posts_like'),
    path('ceate_posts', views.create_posts, name='create_posts'),
    path(
        'update_post/<slug:slug>',
        views.UpdatePost.as_view(),
        name='update_post'
    ),
    path('delete_post/<slug:slug>',
         views.DeletePost.as_view(),
         name='delete_post'),
]
