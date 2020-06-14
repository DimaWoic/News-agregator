from django.forms import ModelForm
from .models import Messages
from captcha.fields import CaptchaField


class MessageForm(ModelForm):
    captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid': 'Неправильный текст'})
    class Meta:
        model = Messages
        fields = ('name', 'email', 'text')