from django import forms
from .models import Contact
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = "__all__"

    # def save(self, commit=True):
    #     instance = super(ContactForm, self).save(commit=False)
    #     instance.name = "Unkown"
    #     if commit:
    #         instance.save()
    #     return instance
