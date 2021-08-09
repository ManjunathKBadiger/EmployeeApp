from django import forms
from .models import Emplyee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Emplyee
        fields = "__all__"
