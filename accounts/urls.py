from .views import SignUpView, guest_login
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    # path('accounts/login/', auth_views.LoginView.as_view() name="login"),
    path('guest', guest_login, name="guest_login"),

]
