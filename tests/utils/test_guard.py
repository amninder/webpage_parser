# -*- coding: utf-8 -*-
import unittest

from webpage_parser.utils.guard import guard


class TestGuard(unittest.TestCase):

    def setUp(self):
        super(TestGuard, self).setUp()

    def test_guard_against_all_exceptions(self):
        """Test for skipping all exceptions."""
        a = guard(lambda: int('p')) or 0
        self.assertEqual(a, 0)

    def test_not_to_guard_against_specific_exeption(self):
        """Test to escape specific exception."""
        with self.assertRaises(ZeroDivisionError):
            guard(lambda: 3/0, against=(ValueError,)) or 0

    def test_to_guard_against_more_than_one_exception(self):
        """Test to escape specific exceptions."""
        a = guard(
            lambda: int('p') / 0, against=(ValueError, ZeroDivisionError)) or 3
        self.assertEqual(a, 3)

    def test_to_catch_against_specific_exception(self):
        """Test to catch specific exception."""
        data = {'a': 3}
        with self.assertRaises(KeyError):
            guard(lambda: data['b'] / 0, against=(ValueError, ZeroDivisionError)) or 3
