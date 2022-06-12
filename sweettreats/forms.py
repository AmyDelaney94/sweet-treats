'''
   Displaying imports at beginning of file
'''
from django import forms
from .models import Comment


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
