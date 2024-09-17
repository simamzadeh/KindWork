from django.urls import path
from django.urls import path
from kind_app.views.gratitude_entry import GratitudeEntryView
from kind_app.views.kind_act import KindActView
from kind_app.views.utils import index
from django.urls import path
from kind_app.views.register import sign_up
from kind_app.views.login import login_request

urlpatterns = [
    path("", index, name="index"),
    path("register/", sign_up, name="register"),
    path("login/", login_request, name="login"),
    path('api/gratitude/', GratitudeEntryView.as_view(), name='gratitude-api'),
    path('api/kind-acts/', KindActView.as_view(), name="kind-acts-api")
]
