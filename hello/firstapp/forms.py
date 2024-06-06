from django import forms


class UserForm(forms.Form):
    combo_text = forms.ComboField(label='Введите данные',
                                  fields=[
                                      forms.CharField(max_length=20),
                                      forms.EmailField()])
    combo_text2 = forms.MultiValueField(label='Комплексное поле',
                                        fields=(
                                            forms.CharField(max_length=20),
                                            forms.EmailField()))
    data_time = forms.SplitDateTimeField(label='Введите дату и время')