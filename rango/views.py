from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {
        'msg': "Guanyin",
        'msg2': "I'm message 2"
    }
    return render(request, 'rango/index.html', context_dict)

def about(request):
    tags_dict = {
        'tag1': 'Nigahi',
    }
    return render(request, 'rango/about.html', tags_dict)