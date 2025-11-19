from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeForms

def liste_employes(request):
    employes = Employee.objects.all()
    return render(request, 'employe/list.html', {'employes': employes})


def ajouter_employe(request):
    form = EmployeForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_employes')
    return render(request, 'employe/formulaire.html', {'form': form, "mode": "ajouter"})

def modifier_employe(request, id):
    employe = get_object_or_404(Employee, id=id)
    form = EmployeForms(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        return redirect('liste_employes')
    return render(request, 'employe/formulaire.html', {'form': form, "mode": "modifier"})

def supprimer_employe(request, id):
    employe = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        employe.delete()
        return redirect('liste_employes')
    return render(request, 'employe/confirme_supprimer.html', {'employe': employe})
