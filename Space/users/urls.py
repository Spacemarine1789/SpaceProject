from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
      'logout/',
      LogoutView.as_view(template_name='users/logout.html'),
      name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
      'change-password/',
      views.PasChange.as_view(template_name='users/pas_change.html'),
      name='pas_change'
    ),
    path(
      'change-password/done/',
      views.PasChangeDone.as_view(template_name='users/pas_done.html'),
      name='pas_done'
    ),
]
