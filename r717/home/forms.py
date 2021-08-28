from django import forms
from django.utils.translation import ugettext_lazy as _

class SendMail(forms.Form):
	name= forms.CharField(widget=forms.TextInput(attrs={'placeholder':   _("Ваше Імя")}))
	email = forms.CharField(label=f'email',
		widget=forms.TextInput(attrs={'placeholder':    _("Ваш телефон")}))
	subject = forms.CharField(label=f"subject",
		widget=forms.TextInput(attrs={'placeholder': 'Тема '}))
	message = forms.CharField(label=f'message',
		widget=forms.Textarea(attrs={'placeholder':    _("Повідомлення")}))
