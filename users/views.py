from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config import settings
from users.forms import UserRegisterForm
from users.models import User


# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm   # кастомное название
    success_url = reverse_lazy('catalog:index')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message='Вы зарегистрировались на площадке "Электронный бутик"',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class MyPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    # form_class = CustomPasswordResetForm
    success_url = reverse_lazy('users:password_reset_done')
    email_template_name = 'users/password_reset_email.html'
    from_email = settings.EMAIL_HOST_USER


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    # form_class = CustomResetConfirmForm
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
