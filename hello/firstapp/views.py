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
   userform = UserForm()
   if request.method == 'POST':
       userform = UserForm(request.POST)
       if userform.is_valid():
           name = userform.cleaned_data['name']
           return HttpResponse("<h2>Введено корректно - {0} </h2>".format(name))

   return render(request, 'firstapp/my_form.html', {'form': userform})
