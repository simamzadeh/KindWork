from django.urls import path
from django.urls import path
from kind_app.views.gratitude_entry import GratitudeEntryView
from kind_app.views.kind_act import KindActView
from kind_app.views.satisfaction import SatisfactionView
from kind_app.views.utils import index
from django.urls import path
from kind_app.views.register import sign_up
from kind_app.views.login import login_request
from kind_app.views.logout import check_authentication, logout_request
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", index, name="index"),
    path("register/", sign_up, name="register"),
    path("login/", login_request, name="login"),
    path('logout/', logout_request, name='logout'),
    path('api/check-auth/', check_authentication, name='check-auth'),
    path('api/gratitude/', GratitudeEntryView.as_view(), name='gratitude-api'),
    path('api/kind-acts/', KindActView.as_view(), name="kind-acts-api"),
    path('api/satisfaction/', SatisfactionView.as_view(), name="satisfaction-api")
]
