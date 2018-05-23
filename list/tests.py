
from django.urls import resolve
from django.test import TestCase
from django.utils import timezone
from datetime import datetime

from .views import ListView, IndexView
from .models import EventModel


class IndexViewTest(TestCase):

    def setUp(self):
        EventModel.objects.create(
            name="The Presidency Election",
            desc="Elect the president of United Continent",
            start_date=datetime(2018, 5, 10, tzinfo=timezone.utc),
            end_date=datetime(2018, 8, 10, tzinfo=timezone.utc),
        )
        EventModel.objects.create(
            name="The Presidency Election",
            desc="Elect the president of United Continent",
            start_date=datetime(2018, 5, 10, tzinfo=timezone.utc),
            end_date=datetime(2018, 8, 10, tzinfo=timezone.utc),
        )
        EventModel.objects.create(
            name="The Presidency Election",
            desc="Elect the president of United Continent",
            start_date=datetime(2018, 5, 10, tzinfo=timezone.utc),
            end_date=datetime(2018, 8, 10, tzinfo=timezone.utc),
        )
        EventModel.objects.create(
            name="The Presidency Election",
            desc="Elect the president of United Continent",
            start_date=datetime(2018, 5, 10, tzinfo=timezone.utc),
            end_date=datetime(2018, 8, 10, tzinfo=timezone.utc),
        )
        EventModel.objects.create(
            name="The Presidency Election",
            desc="Elect the president of United Continent",
            start_date=datetime(2018, 5, 10, tzinfo=timezone.utc),
            end_date=datetime(2018, 8, 10, tzinfo=timezone.utc),
        )
        EventModel.objects.create(
            name="The Presidency Election",
            desc="Elect the president of United Continent",
            start_date=datetime(2018, 5, 10, tzinfo=timezone.utc),
            end_date=datetime(2018, 8, 10, tzinfo=timezone.utc),
        )
        EventModel.objects.create(
            name="The Presidency Election",
            desc="Elect the president of United Continent",
            start_date=datetime(2018, 5, 10, tzinfo=timezone.utc),
            end_date=datetime(2018, 8, 10, tzinfo=timezone.utc),
        )
        EventModel.objects.create(
            name="The Presidency Election",
            desc="Elect the president of United Continent",
            start_date=datetime(2018, 5, 10, tzinfo=timezone.utc),
            end_date=datetime(2018, 8, 10, tzinfo=timezone.utc),
        )
        EventModel.objects.create(
            name="The Staff Election",
            desc="Elect the staff of Supermarket",
            start_date=datetime(2018, 5, 10, tzinfo=timezone.utc),
            end_date=datetime(2018, 8, 10, tzinfo=timezone.utc),
        )
        EventModel.objects.create(
            name="The Headmaster Election",
            desc="Elect the headmaster of Elementary School",
            start_date=datetime(2018, 5, 10, tzinfo=timezone.utc),
            end_date=datetime(2018, 8, 10, tzinfo=timezone.utc),
        )

    def tearDown(self):
        pass

    def test_list_page_resolve_correct(self):
        found = resolve("/")
        self.assertEqual(found.func.view_class, IndexView)

    def test_list_page_render_html_correct(self):
        resp = self.client.get("/")
        self.assertTemplateUsed(resp, "index.html")

    def test_displays_events_on_index_page(self):
        resp = self.client.get("/")
        self.assertContains(resp, "Presidency")

    def test_8_events_per_page_by_default(self):
        resp = self.client.get("/")
        self.assertContains(resp, "Presidency")
        self.assertNotContains(resp, "Staff")

    def test_paginator_page_botton(self):
        resp = self.client.get("/")
        self.assertContains(resp, "下一页")
        self.assertNotContains(resp, "上一页")
        resp = self.client.get("/?page=2")
        self.assertNotContains(resp, "下一页")
        self.assertContains(resp, "上一页")

    def test_first_page_if_no_page_param_passed(self):
        pass


class ListViewTest(TestCase):

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
