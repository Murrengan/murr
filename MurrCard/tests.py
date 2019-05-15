from bs4 import BeautifulSoup

from django.test import TestCase, Client
from django.urls import reverse

from .models import User, Murr, Like


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


class MurrCardSearchTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        user1 = User.objects.create_user(username="user_1", password="1234")
        user2 = User.objects.create_user(username="user_2", password="1234")
        m1 = Murr.objects.create(title="hello1", description="no description", author=user1)
        m2 = Murr.objects.create(title="hello2", description="no description", author=user1)
        m3 = Murr.objects.create(title="hello3", description="no description", author=user1)
        Like.objects.create(murr=m3, murren=user1)
        Like.objects.create(murr=m2, murren=user1)
        Like.objects.create(murr=m2, murren=user2)

    def setUp(self):
        super().setUp()

        self.client = Client()
        assert self.client.login(username="user_1", password="1234")

    def test_simple_query(self):
        res = self.client.get(reverse("search"), data={"q": "hello1"})

        self.assertEqual(200, res.status_code)
        doc = BeautifulSoup(res.content, features="lxml")
        self.assertEqual(1, len(doc.find_all(class_="card")))
        card = doc.find_all(class_="card")[0]
        self.assertEqual("hello1", card.find(class_="card-title").get_text())

    def test_query_with_sorting(self):
        res = self.client.get(reverse("search"), data={
            "sort_by": "-population"
        })

        self.assertEqual(200, res.status_code)
        doc = BeautifulSoup(res.content, features="lxml")
        self.assertEqual(["hello2", "hello3", "hello1"],
                         [card.find(class_="card-title").get_text() for card in doc.find_all(class_="card")])
