from .views import UserCreateView
from django.urls import path
user = UserCreateView
urlpatterns = [
    path('/user', UserCreateView.as_view()),
    path('/login/', UserCreateView.login, name='login'),
]
