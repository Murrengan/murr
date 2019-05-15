from django.test import TestCase

from .models import Murren


class QuestionModelTests(TestCase):
    def test_empty(self):
        self.assertEqual(2, 2)
