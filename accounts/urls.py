from .views import SignUpView, guest_login
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('guest/', guest_login, name="guest_login"),

]
