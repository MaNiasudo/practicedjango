from django.contrib import admin
from base.models import *



class RoomAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["name","created"]

admin.site.register(Room,RoomAdmin) 