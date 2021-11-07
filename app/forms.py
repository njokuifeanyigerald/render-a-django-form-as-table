from django import forms


class DataForm(forms.forms):
    name = forms.CharField(max_length = 200)
    department = forms.CharField(max_length = 200)
    age = forms.IntegerField(
                     help_text = "Enter 6 digit roll number",
                     widget=forms.NumberInput()
                     )
