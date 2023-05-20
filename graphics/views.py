from django.shortcuts import render


def graphics_page(request):
    return render(request, 'graphics.graphics_page.html')


def graphics_add(request):
    return render(request, 'graphics.graphics_add.html')
