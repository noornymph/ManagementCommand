# pylint: disable=all
"""
This module contains the test cases for the 'command' app.
"""

import pytz
from django.core.management import call_command
from django.test import TestCase

from Command.models import PSTDateTime, User


class InsertDummyDataCommandTest(TestCase):
    """Tests for the insert_dummy_data management command."""

    def test_insert_dummy_data(self):
        """Test that dummy users and PST date times are inserted correctly."""
        call_command("insert_dummy_data")

        # Check that 10 dummy users are created
        users = User.objects.all()
        self.assertEqual(users.count(), 10)

        # Check that 100 PST date times are created
        pst_datetimes = PSTDateTime.objects.all()
        self.assertEqual(pst_datetimes.count(), 100)
