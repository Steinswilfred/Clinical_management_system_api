from django.urls import path
from . import views
from . views import DeleteUser,ChangePasswordView

urlpatterns = [
    path('api/cms_auth/signup',views.SignupAPIView.as_view()),
    path("api/cms_auth/delete/<int:passed_id>",DeleteUser),
    path("api/cms_auth/login", views.LoginAPIView.as_view(), name="user-login"),
    path('api/change-password/',ChangePasswordView.as_view(), name='change_password'),
]
