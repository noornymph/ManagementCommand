"""
This module contains the configurations for the 'command' app.
"""

from django.apps import AppConfig


class CommandConfig(AppConfig):
    """
    Class containing configurations.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "Command"
