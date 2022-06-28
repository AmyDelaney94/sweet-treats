'''
   Displaying imports at beginning of file
'''
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    '''
        creating form for creation of comments
    '''
    class Meta:
        '''
            determining what fields are displayed to users
        '''
        model = Comment
        fields = ('body',)


class CreationForm(forms.ModelForm):
    """
    Form class to add a recipe
    """
    class Meta:
        """
        Available fields for recipe creation.
        """
        model = Post
        fields = (
            'title',
            'preparation_time',
            'serving_size',
            'ingredients',
            'instructions',
            'featured_image',
        )

        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(CreationForm, self).__init__(*args, **kwargs)
