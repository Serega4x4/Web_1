from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Person
from django.http import HttpResponseNotFound


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


def edit_form(request, id):
    person = Person.object_person.get(id=id)
    if request.method == 'POST':
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
        return redirect('my_form')
    data = {'person': person}
    return render(request, 'firstapp/edit_form.html', context=data)


def delete(request, id):
    try:
        person = Person.object_person.get(id=id)
        person.delete()
        return redirect('my_form')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Объект не найден</h2>')

