from django.shortcuts import render, redirect
from .forms import UserForm, ImageForm, FileForm, VideoForm, AudioForm
from .models import Person, Image, File, VideoFile, AudioFile
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


def form_up_img(request):
    if request == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    my_text = 'Загруженные изображения'
    my_img = Image.obj_img.all()
    form = ImageForm()
    context = {'my_text': my_text, 'my_img': my_img, 'form': form}
    return render(request, 'firstapp/form_up_img.html', context)


def delete_img(request):
    try:
        img = Image.obj_img.get(id=id)
        img.delete()
        return redirect('form_up_img')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Объект не найден</h2>')


def form_up_pdf(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    my_text = 'Загруженные файлы'
    form = FileForm()
    file_obj = File.objects.all()
    context = {'my_text': my_text, 'file_obj': file_obj, 'form': form}
    return render(request, 'firstapp/form_up_pdf.html', context)


def delete_pdf(request, id):
    try:
        pdf = File.objects.get(id=id)
        pdf.delete()
        return redirect('form_up_pdf')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Объект не найден</h2>')


def form_up_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    my_text = 'Загруженные видеофайлы'
    form = VideoForm()
    file_obj = VideoFile.obj_video.all()
    context = {'my_text': my_text, 'file_obj': file_obj, 'form': form}
    return render(request, 'firstapp/form_up_video.html', context)


def delete_video(request, id):
    try:
        video = VideoFile.obj_video.get(id=id)
        video.delete()
        return redirect('form_up_video')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Объект не найден</h2>')


def form_up_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILE)
        if form.is_valid():
            form.save()
    my_text = 'Загруженные аудиофайлы'
    form = AudioFile()
    file_obj = AudioFile.obj_audio.all()
    context = {'my_text': my_text, 'file_obj': file_obj, 'form': form}
    return render(request, 'firstapp/form_up_audio.html', context)


def delete_audio(request, id):
    try:
        audio = AudioFile.obj_audio.get(id=id)
        audio.delete()
        return redirect('form_up_audio')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Объект не найден</h2>')

