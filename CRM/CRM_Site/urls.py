from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", auth_view.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("record/<int:pk>", views.customer_record, name="record"),
    path("register/", views.register_user, name="register"),
    path("delete_customer/<int:pk>", views.delete_customer, name="delete_customer"),
    path("add_customer/", views.add_customer, name="add_customer"),
    path("update_customer/<int:pk>", views.update_customer, name="update_customer"),
]
