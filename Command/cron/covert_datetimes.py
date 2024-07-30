# pylint: disable=all
"""
Cron job script to convert PST date times to UTC and vice versa every 5 minutes.
"""

import pytz
from django.core.management.base import BaseCommand

from Command.models import PSTDateTime


class Command(BaseCommand):
    """
    A Django management command that converts 10 PST date times to UTC or vice versa every 5 minutes.
    """

    help = "Converts 10 PST date times to UTC or vice versa every 5 minutes"

    def handle(self, *args, **kwargs):
        """
        The main method that handles the command execution.
        Converts 10 PST date times to UTC or vice versa every 5 minutes.
        """
        pst = pytz.timezone("US/Pacific")
        utc = pytz.UTC

        # Fetch the next 10 date times to convert
        pst_datetimes = PSTDateTime.objects.filter(datetime__tzinfo=pst)[:10]
        if not pst_datetimes:
            utc_datetimes = PSTDateTime.objects.filter(datetime__tzinfo=utc)[:10]
            for dt in utc_datetimes:
                dt.datetime = dt.datetime.astimezone(pst)
                dt.save()
            self.stdout.write(self.style.SUCCESS("Converted 10 UTC date times to PST"))
        else:
            for dt in pst_datetimes:
                dt.datetime = dt.datetime.astimezone(utc)
                dt.save()
            self.stdout.write(self.style.SUCCESS("Converted 10 PST date times to UTC"))
