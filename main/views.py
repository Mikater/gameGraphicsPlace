from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, template_name='main/MainPage.html')


def about_us(request):
    return render(request, template_name='main/about.html')


def profile(request):
    return render(request, template_name='main/profile.html')
