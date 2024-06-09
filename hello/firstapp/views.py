from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.shortcuts import render
from django.template.response import TemplateResponse
from .forms import UserForm


def index(request):
    my_text = 'Изучаем формы Django'
    context = {'my_text': my_text}
    return render(request, 'firstapp/index.html', context)


def about(request):
    return render(request, 'firstapp/about.html')


def contact(request):
    return render(request, 'firstapp/contact.html')


def my_form(request):
    if request.method=='POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = request.POST.get('name')
            age = request.POST.get('age')
            output = '<h2>Пользователь</h2><h3>Имя - {0}, '\
                'Возраст - {1} </h3>'.format(name, age)
            return HttpResponse(output)
    userform = UserForm()
    return render(request, 'firstapp/my_form.html', {'form': userform})
