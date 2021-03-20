from django.contrib import admin

from .models import Artist, Possession, Record

admin.site.register(Artist)
admin.site.register(Possession)
admin.site.register(Record)
