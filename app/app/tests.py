"""
Sample tests: must be either tests.py or tests/ dir, not BOTH.
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together. test_ must be in the function name """
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test adding numbers together."""
        res = calc.subtract(6, 5)

        self.assertEqual(res, 1)
