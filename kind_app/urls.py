from django.urls import path
from kind_app.views.achievement import AchievementView
from kind_app.views.highlight import HighlightView
from kind_app.views.kudos import KudosView
from kind_app.views.satisfaction import SatisfactionView
from kind_app.views.utils import index, get_csrf_token
from kind_app.views.register import sign_up
from kind_app.views.login import login_request
from kind_app.views.logout import check_authentication, logout_request
from kind_app.views.lockout import lockout
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import ensure_csrf_cookie

urlpatterns = [
    path("", index, name="index"),
    path("register/", sign_up, name="register"),
    path("login/", login_request, name="login"),
    path('logout/', logout_request, name='logout'),
    path('locked/', lockout, name='account_locked'),
    path('api/check-auth/', check_authentication, name='check-auth'),
    path('api/security/get-csrf-token/', ensure_csrf_cookie(get_csrf_token), name='get-csrf-token'),
    path('api/kudos/', KudosView.as_view(), name='kudos-api'),
    path('api/achievements/', AchievementView.as_view(), name="achievements-api"),
    path('api/highlights/', HighlightView.as_view(), name="highlight-api"),
    path('api/satisfaction/', SatisfactionView.as_view(), name="satisfaction-api")
]
