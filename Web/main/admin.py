from django.contrib import admin
from main.models import Message, Room


admin.site.register(Room)
admin.site.register(Message)