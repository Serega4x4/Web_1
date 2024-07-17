from django import forms
from .models import Person, Image, File, VideoFile


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


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoFile
        fields = '__all__'

