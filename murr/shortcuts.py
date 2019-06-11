from decimal import Decimal
from string import digits
from django.core.paginator import Paginator


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


class CustomPaginator(Paginator):
    def validate_number(self, number):
        """Validate the given 1-based page number."""
        try:
            if isinstance(number, float) and not number.is_integer():
                raise ValueError
            number = int(number)
        except (TypeError, ValueError):
            return 1
        if number < 1:
            return 1
        if number > self.num_pages:
            if number == 1 and self.allow_empty_first_page:
                pass
            else:
                return self.num_pages
        return number