from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get("email")

        # Check if the email is already associated with an existing user
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use!")

        return email

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
