from django.shortcuts import render

from .models import Menu


def index(request):
    return render(request, 'index.html', {'menus': Menu.objects.all()})


def draw_menu(request, path):
    splitted_path = path.split('/')
    assert len(splitted_path) > 0, ('= Функция Draw_menu не сработала =')
    print(splitted_path)
    return render(
        request, 'index.html', {'menu_name': splitted_path[0], 'menu_item': splitted_path[-1]})
