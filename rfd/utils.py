"""This module provides utility functions that are used within rfd"""


def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False
