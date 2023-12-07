# views.py
from django.shortcuts import render

def custom_error_404(request, exception):
    return render(request, '404.html', status=404)

def custom_error_500(request):
    return render(request, '500.html', status=500)
