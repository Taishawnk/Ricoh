from django.shortcuts import render , HttpResponse


def index(request):
    return render(request, 'main.html')

def wiki_view(request):
    return render(request, 'wiki.html')
    # Create your views here.
