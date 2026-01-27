from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("record/<int:pk>", views.customer_record, name="record"),
    path("delete_customer/<int:pk>", views.delete_customer, name="delete_customer"),
    path("update_customer/<int:pk>", views.update_customer, name="update_customer"),
]
