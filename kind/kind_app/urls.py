from django.urls import path
from django.urls import path
from kind_app.views.gratitude_entry import GratitudeEntryView
from kind_app.views.utils import index

from . import views

urlpatterns = [
    path("", index, name="index"),
    path('api/gratitude/', GratitudeEntryView.as_view(), name='gratitude-entry'),
]
