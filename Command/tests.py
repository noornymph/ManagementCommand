# pylint: disable=all
"""
This module contains the test cases for the 'command' app.
"""

from datetime import datetime

import pytz
from Command.models import PSTDateTime, User
from django.core.management import call_command
from django.test import TestCase


class InsertDummyDataCommandTest(TestCase):
    """Tests for the insert_dummy_data management command."""

    def test_insert_dummy_data(self):
        """Test that dummy users and PST date times are inserted correctly."""

        # Check that database is initaially empty
        previous_users = User.objects.all()
        self.assertEqual(previous_users.count(), 0)

        pst_datetimes = PSTDateTime.objects.all()
        self.assertEqual(pst_datetimes.count(), 0)

        call_command("insert_dummy_data")

        # Check that 10 dummy users are created
        current_users = User.objects.all()
        self.assertEqual(current_users.count(), 10)

        # Check that 100 PST date times are created
        pst_datetimes = PSTDateTime.objects.all()
        self.assertEqual(pst_datetimes.count(), 100)


class UpdateDateTimeCommandTest(TestCase):
    """Tests for the insert_dummy_data management command."""

    def setUp(self):
        # Set up initial data
        pst = pytz.timezone("US/Pacific")
        pst_datetimes = []

        for i in range(200):
            pst_time = pst.localize(datetime.now())
            pst_datetimes.append(PSTDateTime(datetime=pst_time, is_utc=False))

        PSTDateTime.objects.bulk_create(pst_datetimes)

    def test_update_date_time(self):
        """Test that dates and times are updated correctly correctly."""

        call_command("update_date_times")

        # Check that the first 10 objects have been converted to UTC
        updated_objects = PSTDateTime.objects.filter(is_utc=True)
        self.assertEqual(updated_objects.count(), 10)

        # Run the command again and check the objects have been converted back to PST
        call_command("update_date_times")
        self.assertTrue(PSTDateTime.objects.filter(is_utc=False).exists())
