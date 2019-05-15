from django.test import TestCase, Client
from django.urls import reverse

from .models import User, Murr


class MurrCardTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        User.objects.create_user(username="admin", password="1234")

    def setUp(self):
        super().setUp()

        self.client = Client()
        assert self.client.login(username="admin", password="1234")

    def test_get_murrs(self):
        res = self.client.get('/murrs/', follow=True)
        print(res.content)

    def test_crud_murr(self):
        # create
        res = self.client.post(reverse("murr_create"), {
            "title": "new",
            "description": "new",
            "content": "<p>1234</p>",
            "tags": "",
            "cover": "",
            "submit": "Сохранить",
        }, follow=True)

        self.assertEqual(200, res.status_code)
        murr_id = res.redirect_chain[-1][0].split('/')[-1]

        self.assertEqual(1, Murr.objects.count())

        # read
        res = self.client.get(reverse("murr_detail", args=[murr_id, ]), follow=True)
        self.assertEqual(200, res.status_code)

        # update title
        res = self.client.post(reverse("murr_update", args=[murr_id, ]), follow=True, data={
            "title": "new_new",
            "description": "new",
            "content": "<p>1234</p>",
            "tags": "",
            "cover": "",
            "submit": "Сохранить",
        })

        self.assertEqual(200, res.status_code)
        self.assertEqual("new_new", Murr.objects.first().title)
