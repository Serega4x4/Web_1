from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя клиента', help_text='ФИО не более 100 символов')
    basket = forms.BooleanField(label='Положить товар в корзину', required=False)
    ling = forms.ChoiceField(label='Выберите язык',
                             choices=((1, 'Английский'),
                                      (2, 'Немецкий'),
                                      (3, 'Французский')))
    data = forms.DateField(label='Введите дату')
    data_time = forms.DateTimeField(label='Введите дату И ВРЕМЯ')
    num = forms.DecimalField(label='Введите десятичное число', decimal_places=2)
    time_delta = forms.DurationField(label='Введите промежуток времени')
    email = forms.EmailField(label='Электроннный адрес', help_text='Обязательный символ "@"!')
    file = forms.FileField(label='Файл')
    image = forms.ImageField(label='Изображение')
    jsON = forms.JSONField(label='Данные формата JSON')
    slug_text = forms.SlugField(label='Введите текст')
    url = forms.URLField(label='Введите URL', help_text='например www.yandex.ru')
    