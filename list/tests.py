
from django.urls import resolve
from django.test import TestCase

from .views import ListView


class ListPageTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_list_page_resolve_correct(self):
        found = resolve("/list/")
        self.assertEqual(found.func.view_class, ListView)

    def test_list_page_render_html_correct(self):
        resp = self.client.get("/list/")
        self.assertTemplateUsed(resp, "list.html")
