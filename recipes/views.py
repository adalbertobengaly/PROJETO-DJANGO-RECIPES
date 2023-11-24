from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Adalberto Bengaly',
    })


def sobre(request):
    return render(request, 'recipes/sobre.html')


def contato(request):
    return render(request, 'recipes/contato.html')
