from django.contrib.auth.forms import UserCreationForm

from catalog.forms import FormStyleMixin
from users.models import User


class UserRegisterForm(FormStyleMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'phone', 'country', 'avatar', 'password1', 'password2')
        template_name = 'users/register.html'
