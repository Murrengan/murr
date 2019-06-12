from decimal import Decimal
from string import digits
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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


class MurrenganPaginator(Paginator):
    def validate_number(self, number):
        try:
            number = super().validate_number(number)
        except PageNotAnInteger:
            number = 1
        except EmptyPage:
            number = 1 if parse_int(number) < 1 else self.num_pages
        return number