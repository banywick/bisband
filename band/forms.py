from django import forms
from captcha.fields import CaptchaField
from .models import Application

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Application
        fields = ['name', 'email', 'text']
        labels = {
            'name': '',
            'email': '',
            'text': '',
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Ваше имя',
            'required': 'required',
            'label': 'Леха'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Ваш email',
            'required': 'required'
        })
        self.fields['text'].widget.attrs.update({
            'placeholder': 'Ваше сообщение',
            'required': 'required'
        })
