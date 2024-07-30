# pylint: disable=all
"""
This module contains a Django management command to update PST date times
to UTC and then back to PST in a rotating manner. The command updates a
batch of 10 date times every 5 minutes.
"""

import pytz
from django.core.management.base import BaseCommand

from Command.models import PSTDateTime


class Command(BaseCommand):
    """
    Management command to update PST date times to UTC and then convert
    them back to PST once 100 date times have been converted.
    """

    help = "Updates PST date times to UTC and then back to PST in a rotating manner"

    def handle(self, *args, **kwargs):
        """
        Executes the command to update date times.
        """

        pst_datetimes = PSTDateTime.objects.filter(is_utc=False)[:10]

        if not pst_datetimes:
            self.stdout.write(self.style.SUCCESS("No PST date times to update"))
            return

        utc = pytz.utc
        for pst_datetime in pst_datetimes:
            pst_datetime.datetime = pst_datetime.datetime.astimezone(utc)
            pst_datetime.is_utc = True
            pst_datetime.save()

        if PSTDateTime.objects.filter(is_utc=True).count() >= 100:
            utc_datetimes = PSTDateTime.objects.filter(is_utc=True)[:10]
            pst = pytz.timezone("US/Pacific")
            for utc_datetime in utc_datetimes:
                utc_datetime.datetime = utc_datetime.datetime.astimezone(pst)
                utc_datetime.is_utc = False
                utc_datetime.save()

        self.stdout.write(self.style.SUCCESS("Successfully updated date times"))
