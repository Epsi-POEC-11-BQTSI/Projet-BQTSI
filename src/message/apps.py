""" Gestion de la configuration des messages"""
from django.apps import AppConfig


class MessageConfig(AppConfig):
    """ BigAutoField auto-incrémente les messages à chaque instance créée d'un champ message """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'message'
