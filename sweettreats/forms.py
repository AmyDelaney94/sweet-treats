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
    '''
    Form class to add a recipe
    '''
    class Meta:
        '''
        Using Post model, choose fields to update.
        '''
        model = Post
        fields = (
            'title',
            'author',
            'preparation_time',
            'serving_size',
            'ingredients',
            'instructions',
            'featured_image',
        )

        widgets = {
            'ingredients': SummernoteWidget(attrs={
                'summernote': {'width': '350px', 'height': '400px'}}),
            'instructions': SummernoteWidget(attrs={
                'summernote': {'width': '350px', 'height': '400px'}}),
        }

    def __init__(self, *args, **kwargs):
        super(CreationForm, self).__init__(*args, **kwargs)


class UpdateRecipeForm(forms.ModelForm):
    """ Update a Post Form """
    class Meta:
        """
        Get post model, choose fields to update and add summernote widget
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
            'ingredients': SummernoteWidget(attrs={
                'summernote': {'width': '350px', 'height': '400px'}}),
            'instructions': SummernoteWidget(attrs={
                'summernote': {'width': '350px', 'height': '400px'}}),
        }
