from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя Клиента',
                           widget=forms.TextInput(attrs={'class': 'myfield'}))
    age = forms.IntegerField(label='Возраст клиента',
                             widget=forms.TextInput(attrs={'class': 'myfield'}))
    # required_css_class = 'field'
    # error_css_class = 'error'
