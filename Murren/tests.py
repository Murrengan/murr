from django.test import TestCase, Client
from django.urls import reverse

from .models import Murren


class QuestionModelTests(TestCase):
    def test_empty(self):
        self.assertEqual(2, 2)
