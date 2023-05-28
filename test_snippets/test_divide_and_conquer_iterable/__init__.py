"""
Divide and conquer iterable unit tests.
"""

from typing import NoReturn, Iterable
from unittest import TestCase

from snippets.divide_and_conquer_iterable import divide_and_conquer_iterable


def dummy_logic(iterable: Iterable) -> NoReturn:
    """
    Mock function to raise an exception when a particular value is encountered in an iterable.

    To appropriately replicate the sample scenario, this function cannot provide any indication which item the exception
    was encountered in.

    :param iterable: Iterable to process.
    :return: Nothing.
    """

    for item in iterable:
        if item == NotImplemented:
            raise Exception("Bad Item")


class DivideAndConquerIterableTests(TestCase):
    """
    Dive and conquer unit tests.
    """

    def test_all_ok(self) -> NoReturn:
        """
        Validate the algorithm can handle when no items in the input iterable result in an exception being raised.
        :return: None.
        """

        data = [1, 2, 3, 4, 5, 6]
        bad_results, good_results = divide_and_conquer_iterable(
            iterable=data, action=dummy_logic
        )

        self.assertEqual(([], sorted(data)), (bad_results, sorted(good_results)))

    def test_one_bad(self) -> NoReturn:
        """
        Validate the algorithm appropriately handles when one item in the input iterable is bad.

        :return: None.
        """

        bad_results, good_results = divide_and_conquer_iterable(
            iterable=[1, 2, 3, 4, 5, NotImplemented], action=dummy_logic
        )

        self.assertEqual(
            first=([NotImplemented], [1, 2, 3, 4, 5]),
            second=(bad_results, sorted(good_results)),
        )

    def test_two_bad(self) -> NoReturn:
        """
        Validate the algorithm appropriately handles when two items in the input iterable are bad.

        :return: None.
        """

        bad_results, good_results = divide_and_conquer_iterable(
            iterable=[NotImplemented, 2, 3, 4, 5, NotImplemented], action=dummy_logic
        )

        self.assertEqual(
            first=([NotImplemented, NotImplemented], [2, 3, 4, 5]),
            second=(bad_results, sorted(good_results)),
        )

    def test_all_bad_even_length(self) -> NoReturn:
        """
        Validate the algorithm appropriately handles when all items in the input iterable are bad and the iterable
        contains an even number of items.

        :return: None.
        """

        data = [NotImplemented, NotImplemented, NotImplemented, NotImplemented]

        self.assertEqual(
            first=(data, []),
            second=divide_and_conquer_iterable(iterable=data, action=dummy_logic),
        )

    def test_all_bad_odd_length(self) -> NoReturn:
        """
        Validate the algorithm appropriately handles when all items in the input iterable are bad and the iterable
        contains an odd number of items.

        :return: None.
        """

        data = [NotImplemented, NotImplemented, NotImplemented]
        self.assertEqual(
            first=(data, []),
            second=divide_and_conquer_iterable(iterable=data, action=dummy_logic),
        )
