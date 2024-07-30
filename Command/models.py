"""
This module contains the models for the 'command' app. It includes
definitions for the database models used in the application.
"""

from django.db import models


class User(models.Model):
    """
    Represents a user in the system.
    """

    username = models.CharField(max_length=100)
    email = models.EmailField()


class PSTDateTime(models.Model):
    """
    Represents a date and time in the Pacific Standard Time (PST) timezone.
    """

    datetime = models.DateTimeField()
    is_utc = models.BooleanField(default=False)
