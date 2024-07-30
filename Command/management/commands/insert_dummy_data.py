# pylint: disable=all

"""
Management command to insert dummy users and PST date times into the database.
"""

import pytz
from django.core.management.base import BaseCommand
from django.utils import timezone

from Command.models import PSTDateTime, User


class Command(BaseCommand):
    """
    A Django management command to insert dummy users and PST date times into the database.
    """

    help = "Inserts dummy users and PST date times into the database"

    def handle(self, *args, **kwargs):
        """
        The main method that handles the command execution.
        Inserts dummy users using bulk_create and inserts 100 PST date times.
        """

        users = [
            User(username=f"user{i}", email=f"user{i}@example.com") for i in range(10)
        ]
        User.objects.bulk_create(users)

        pst = pytz.timezone("US/Pacific")
        pst_datetimes = [
            PSTDateTime(datetime=timezone.now().astimezone(pst)) for _ in range(100)
        ]
        PSTDateTime.objects.bulk_create(pst_datetimes)

        self.stdout.write(
            self.style.SUCCESS("Successfully inserted dummy users and PST date times")
        )
