from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Grape
# Create your views here.

def grape_list(request):
    grapes = Grape.objects.all()
    return render(request, 'grapes/grape_list.html', {'grapes': grapes})

def grape_detail(request, pk):
    grape = get_object_or_404(Grape, pk=pk)
    return render(request, 'grapes/grape_detail.html', {'grape': grape})

# def grapes_home(request):
#     grapes = Grape.objects.all()
#     return render(request, 'grapes/grape_list.html', {'grapes': grapes})
