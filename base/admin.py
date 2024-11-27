from django.contrib import admin
from base.models import *



class RoomAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["name","host","topic","created"]

admin.site.register(Room,RoomAdmin) 



class TopicAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["name","created"]

admin.site.register(Topic,TopicAdmin) 



class MessageAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["user","room","created"]

admin.site.register(Message,MessageAdmin) 