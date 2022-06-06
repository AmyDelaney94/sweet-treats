'''
    Documenting inports at top of file.
'''
from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    '''
        Code block used to format post layout on main page
    '''
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
