from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from .forms import UserForm
from .models import Person


def index(request):
    my_text = 'Изучаем формы Django'
    people_kol = Person.object_person.count()
    context = {'my_text': my_text, 'people_kol': people_kol}
    return render(request, 'firstapp/index.html', context)


def about(request):
    return render(request, 'firstapp/about.html')


def contact(request):
    return render(request, 'firstapp/contact.html')


def my_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    my_text = 'Сведения о клиентах'
    people = Person.object_person.all()
    form = UserForm()
    context = {'my_text': my_text, 'people': people, 'form': form}
    return render(request, 'firstapp/my_form.html', context)
