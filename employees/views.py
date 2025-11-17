from django.shortcuts import render
from .models import Employee

def liste_employes(request):
    employes = Employee.objects.all()
    return render(request, 'employe/list.html', {'employes': employes})
