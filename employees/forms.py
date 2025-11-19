from django import forms
from .models import Employee


class EmployeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['nom', 'prenom', 'address', 'email', 'poste', 'salaire']
        widgets = {
            'nom' : forms.TextInput(attrs= {
                'class' : "input w-full",
                'placeholder' : 'Nom'
            }),
             'prenom' : forms.TextInput(attrs= {
                'class' : "input w-full",
                'placeholder' : 'Prenom'
            }),
             'address' : forms.TextInput(attrs= {
                'class' : "input w-full",
                'placeholder' : 'Address'
            }),
             'email' : forms.TextInput(attrs= {
                'class' : "input w-full",
                'placeholder' : 'E-mail'
            }),
             'poste' : forms.TextInput(attrs= {
                'class' : "input w-full",
                'placeholder' : 'Poste'
            }),

             'salaire' : forms.TextInput(attrs= {
                'class' : "input w-full",
                'placeholder' : 'Salaire'
            }),
        }