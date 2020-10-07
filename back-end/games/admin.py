from django.contrib import admin

# Register your models here.
from .models import Game, Record
admin.site.register(Game)
admin.site.register(Record)
