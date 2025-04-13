from django.shortcuts import render

def cursos_ead(request):
    return render(request, 'cursos/index.html')
