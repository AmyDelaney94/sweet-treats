'''
    Documenting imports at beginning of file
'''
from django.apps import AppConfig


class SweettreatsConfig(AppConfig):
    '''
        class to define app name
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sweettreats'
