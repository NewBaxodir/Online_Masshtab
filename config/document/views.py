from django.shortcuts import render, get_object_or_404
from .models import (
    DocumentFile,
    Fanlar,
    Kategoriya
)


def HomeView(request):
    fanlar = Fanlar.objects.all()
    kategoriyalar = Kategoriya.objects.all()
    search_input = request.GET.get("search_input", "")
    if search_input == "":
        db = None
    else:
        db = DocumentFile.objects.filter(name__contains = search_input).all()[:2]
    data = {
        'fanlar': fanlar,
        'ktg': kategoriyalar,
        'db': db,
        'search_i': search_input,
    }
    return render(request, 'home.html', data)


def FanlarView(request, pk):
    fan_name = get_object_or_404(Fanlar, pk=pk)
    data = DocumentFile.objects.filter(fan_id=pk).order_by('pk')
    fanlar = Fanlar.objects.all()
    return render(request, 'fanlar.html', {
        'data': data,
        'fan': fanlar,
        'fan_name': fan_name,
    })


def TurlarView(request, pk):
    tur_nomi = get_object_or_404(Kategoriya, pk=pk)
    data = DocumentFile.objects.filter(category_id=pk).order_by('pk')
    ktg = Kategoriya.objects.all()

    return render(request, 'kategory.html', {
        'ktg': ktg,
        'data': data,
    })