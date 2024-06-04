from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    my_kv = ['I квартал ->', 'II квартал ->', 'III квартал ->', 'IV квартал ->']
    my_month = ['Январь', 'Февраль', 'Март',
                'Апрель', 'Май', 'Июнь',
                'Июль', 'Август', 'Сентябрь',
                'Октябрь', 'Ноябрь', 'декабрь']
    context = {'my_month': my_month, 'my_kv': my_kv}
    return render(request, "firstapp/index.html", context)


def about(request):
    return render(request, 'firstapp/about.html')


def contact(request):
    return render(request, 'firstapp/contact.html')
