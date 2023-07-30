from django.shortcuts import render, redirect


def home_page(request):
    return render(request, 'core/home-page.html')


def about_page(request):
    return render(request, 'core/about-page.html')


def specials_page(request):
    return render(request, 'menu/special-page.html')


def events_page(request):
    return render(request, 'core/events-page.html')


def chefs_page(request):
    return render(request, 'core/chefs-page.html')


def gallery_page(request):
    return render(request, 'core/gallery-page.html')


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler403(request, exception):
    return redirect('home page')
