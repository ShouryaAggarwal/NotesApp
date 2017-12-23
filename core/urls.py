from django.conf.urls import url, include
from django.contrib import admin
from .views import index_view, add_note

app_name = "core"

urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^addnote/', add_note, name='addnote'),

]