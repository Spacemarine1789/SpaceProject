from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordChangeView,
)

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


class PasChange(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('users:pas_done')
    template_name = 'users/pas_change.html'


class PasChangeDone(PasswordChangeDoneView):
    template_name = 'users/pas_done.html'
