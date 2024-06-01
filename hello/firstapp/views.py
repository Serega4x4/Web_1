from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    header = "Развлетвления в шаблонах"
    num = 2
    var1 = "Это первая ветка в инструкции if"
    var2 = "Это вторая ветка в инстукции if"
    data = {
        'header': header,
        "num": num,
        "var1": var1,
        "var2": var2,
    }

    return TemplateResponse(request, "firstapp/index_app1.html", data)


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponseRedirect("/about")


def products(request, productid=1):
    category = request.GET.get('cat', 'Не задана')
    output = '<h2>продукт № {0} Категория: {1}</h2>'.format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get('id', 'Не задано')
    name = request.GET.get('name', 'Не задано')
    output = "<h2>Пользователь</h2><h3>id: {0} Имя:{1}</hЗ>".format(id, name)
    return HttpResponse(output)


def details(request):
    return HttpResponsePermanentRedirect("/")


def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорретные данные")
    if age > 17:
        return HttpResponse("Доступ разрешен")
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")
