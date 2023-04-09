from django.shortcuts import render
from django.http import HttpResponse
from .models import Sorts_of_grapes
# Create your views here.

def grapes_home(request):
    sorts = Sorts_of_grapes.objects.all()
    return render(request, 'grapes/grapes_home.html', {'sorts': sorts})
