
from django.views.generic import View
from django.shortcuts import render


class ListView(View):

    @staticmethod
    def get(request):
        return render(request, "list.html", {
            "vote_name": "TEST",
        })

    @staticmethod
    def post(request):
        pass
