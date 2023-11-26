from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Adalberto Bengaly',
    })


def recipe(request, id):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Adalberto Bengaly',
    })
