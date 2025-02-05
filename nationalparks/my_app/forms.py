from django import forms
from .models import Trail


class TrailForm(forms.ModelForm):
    class Meta:
        model = Trail
        fields = ['name', 'difficulty']
        # widgets = {
        #     'name': forms.DateInput(
        #         format=('%Y-%m-%d'),
        #         attrs={
        #             'placeholder': 'Select a name',
        #             'type': 'name'
        #         }
        #     ),
        # }



        
        