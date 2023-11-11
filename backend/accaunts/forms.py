from django import forms
from django.contrib.auth import authenticate, get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model



User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput,
        strip=False,
        help_text="Your password must contain at least 8 characters.",
    )
    password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput,
    )
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        email_check = User.objects.filter(email=email)
        if email_check.exists():
            raise forms.ValidationError('This Email already exists')
        if len(password) < 5:
            raise forms.ValidationError('Your password should have more than 5 characters')
        if self.password1 != self.password2:
            raise forms.ValidationError('Your password do not match')
        return super(UserRegisterForm, self).clean(*args, **kwargs)

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField()

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput,
        strip=False,
        help_text="Your password must contain at least 8 characters.",
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput,
    )
