from django.shortcuts import render

def vista_base(request):
    return render(request, 'base.html')

def vista_inicio(request):
    return render(request, 'inicio.html')