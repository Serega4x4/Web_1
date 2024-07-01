from django import forms
from .models import Person, Image


class UserForm(forms.ModelForm):
    name = forms.CharField(label='Имя Клиента',
                           widget=forms.TextInput(attrs={'class': 'myfield'}))
    age = forms.IntegerField(label='Возраст клиента',
                             widget=forms.TextInput(attrs={'class': 'myfield'}))

    class Meta:
        model = Person
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
