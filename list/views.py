
from django.views.generic import View
from django.shortcuts import render
from django.core.paginator import EmptyPage
from pure_pagination import Paginator, PageNotAnInteger

from .models import EventModel
from variables import EVENT_ITEMS_EVERY_PAGE


class IndexView(View):

    @staticmethod
    def get(request):
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        all_events = EventModel.objects.all().order_by("-add_time")
        paginator = Paginator(all_events, EVENT_ITEMS_EVERY_PAGE, request=request)
        try:
            events = paginator.page(page)
        except EmptyPage:
            events = paginator.page(all_events.count() // EVENT_ITEMS_EVERY_PAGE + 1)
        return render(request, "index.html", {
            "events": events,
        })

    @staticmethod
    def post(request):
        pass


class ListView(View):

    @staticmethod
    def get(request):
        return render(request, "list.html", {
            "vote_name": "TEST",
        })

    @staticmethod
    def post(request):
        pass
