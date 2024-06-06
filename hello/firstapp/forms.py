from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя Клиента')
    age = forms.IntegerField(label='Возраст клиента')
