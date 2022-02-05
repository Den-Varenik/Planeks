from django.urls import path

from account.views import UserLoginView, logout_user

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
]
