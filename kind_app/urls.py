from django.urls import path
from django.urls import path
from kind_app.views.gratitude_entry import GratitudeEntryView
from kind_app.views.utils import index
from django.urls import path
from kind_app.views.register import sign_up
from kind_app.views.login import login_request

urlpatterns = [
    path("", index, name="index"),
    path("register/", sign_up, name="register"),
    path("login/", login_request, name="login"),
    # path("gratitude", gratitude, name="gratitude"),
    path('api/gratitude/', GratitudeEntryView.as_view(), name='gratitude-api'),
]
