from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 15)
    last_name = forms.CharField(max_length = 15)
    middle_name = forms.CharField(max_length = 15)
    date = forms.DateField()
    foto = forms.FileField(upload_to = None)
    stud_bilet = forms.CharField(max_length = 100)
    stud_group = forms.CharField(max_length = 200)