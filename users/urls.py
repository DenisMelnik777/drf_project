from django.urls import path
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views import UserListView, UserCreateView

app_name = UsersConfig.name


urlpatterns = [
                  path('user/', UserListView.as_view()),
                  path('user/create/', UserCreateView.as_view()),

              ]