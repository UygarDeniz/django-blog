from django.urls import path, reverse_lazy
from .views import RegisterView, me
from .forms import CustomAuthenticationForm
from django.contrib.auth.views import (
    LogoutView, 
    LoginView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView 
)

app_name = "user"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(template_name="user/login.html", authentication_form=CustomAuthenticationForm), name="login"),
    path("me/", me, name="profile"),
]