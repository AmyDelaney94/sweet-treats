'''
    Documenting inports at top of file.
'''
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, CreationForm


class PostList(generic.ListView):
    '''
        View to show all recipe posts on page
    '''
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    '''
        View used to display selected posts
    '''
    def get(self, request, slug, *args, **kwargs):
        '''
           Setting query to find posts and approved comments.
           Comments are displayed in ascending order
        '''
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "posts.html",
            {
               "post": post,
               "comments": comments,
               "commented": False,
               "liked": liked,
               "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        '''
           Setting query to display posts and approved comments.
           Comments are displayed in ascending order.
           Comments must be approved to be displayed.
        '''
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "posts.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    '''
        Code to allow users to like posts
    '''
    def post(self, request, slug, *args, **kwargs):
        '''
            This method displays like status
        '''
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('posts', args=[slug]))


def createposts(request):
    '''
    Alows user to share and post a recipe
    '''
    posts_form = CreationForm(request.POST or None, request.FILES or None)
    context = {
        'posts_form': posts_form,
    }

    if request.method == "POST":
        posts_form = CreationForm(request.POST, request.FILES)
        if posts_form.is_valid():
            print('valid')
            posts_form.instance.author = request.user
            posts_form.instance.status = 1
            posts = posts_form.save(commit=False)

            posts.save()
            return redirect('index')
        else:
            print('invalid')
    else:
        posts_form = CreationForm()
    return render(request, "create_posts.html", context)


class UpdateRecipe(UpdateView):
    '''
    View to update a recipe
    '''
    model = Post
    template_name = 'update_post.html'
    form_class = CreationForm


class DeleteRecipe(DeleteView):
    '''
    View to delete a recipe
    '''
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('user_recipes')
