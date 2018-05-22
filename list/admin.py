
from django.contrib import admin

from .models import EventModel, PlayerModel, PicsModel, VoteModel


class EventModelAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "desc",
        "start_date",
        "end_date",
        "add_time",
    ]
    search_fields = [
        "name",
        "desc",
    ]
    list_filter = [
        "name",
        "desc",
        "start_date",
        "end_date",
        "add_time",
    ]


admin.site.register(EventModel, EventModelAdmin)
