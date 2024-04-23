from django.urls import path
from . import views

urlpatterns = [
    path("api/cms_auth/login", views.LoginAPIView.as_view(), name="user-login"),
]
