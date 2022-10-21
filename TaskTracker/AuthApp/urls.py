from django.urls import path
from .views import login, signin

urlpatterns = [
    path('login', login.as_view()),
    path('signin', signin.as_view()),
]
