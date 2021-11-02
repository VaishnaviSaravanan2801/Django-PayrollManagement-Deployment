from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="login"),
	path("logout/", views.logout, name="logout"),

]