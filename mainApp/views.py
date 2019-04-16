from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['If you have any quetions, please do not hesitate to call me', '(819) 068-68-68', 'email@email.com']})
