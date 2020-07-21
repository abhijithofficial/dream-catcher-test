from django.urls import path
from . import views

urlpatterns = [
    path('userdata/', views.UserList.as_view()),

    # User Authentication
    path('register/', views.UserSignUp.as_view()),
    path('login/', views.UserLogin.as_view()),
]
