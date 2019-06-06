from decimal import Decimal
from string import digits


def is_digit(char):
    return char in digits + '+-.' and char or ''


def strip_int(text):
    return ''.join([is_digit(c) for c in text])


def parse_int(value):
    if not value:
        return None

    if isinstance(value, (int, float, Decimal)):
        return int(value)

    try:
        return int(float(strip_int(value)))
    except ValueError:
        return None
