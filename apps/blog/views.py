from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from . import models

def home(request):
    articulo_pagina = Paginator(models.Articulo.objects.filter(publicado=True), 2)
    pagina = request.GET.get('pagina')
    contexto = { 'articulos': articulo_pagina.get_page(pagina) }
    return render(request, 'blog/home.html', contexto)


def post(request, articulo_id):
    try:
        contexto = { 'articulo': get_object_or_404(models.Articulo, id=articulo_id ) }
        return render(request, 'blog/post.html', contexto)
    except:
        return render(request, 'blog/404.html')


def author(request, autor_id):
    try:
        contexto = { 'autor': get_object_or_404(User, id=autor_id ) }
        return render(request, 'blog/author.html', contexto)
    except:
        return render(request, 'blog/404.html')


def category(request, categoria_id):
    try:
        contexto = { 'categoria': get_object_or_404(models.Categoria, id=categoria_id ) }
        return render(request, 'blog/category.html', contexto)
    except:
        return render(request, 'blog/404.html')


def dates(request, month_id, year_id):
    meses = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre',
    }

    if month_id < 1 or month_id > 12:
        return render(request, 'blog/404.html')
    
    contexto = { 
        'articulos': models.Articulo.objects.filter(publicado=True, creacion__month=month_id, creacion__year=year_id),
        'month': meses[month_id],
        'year': year_id
        }
    return render(request, 'blog/dates.html', contexto)