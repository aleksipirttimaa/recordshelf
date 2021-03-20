from django.contrib import admin
from django.urls import include, path

from records.views import exorcise, index, logout_and_redirect, possess, records, shelf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index),
    path('records/', records),
    path('records/<int:record_id>/possess', possess),
    path('records/<int:record_id>/exorcise', exorcise),
    path('shelf/', shelf),
    path('logout/', logout_and_redirect),
]
