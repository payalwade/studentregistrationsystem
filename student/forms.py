from django import forms
class StudForm(forms.Form):
    s_name = forms.CharField(max_length=30,label='Student Name')
    s_class = forms.CharField(max_length=30,label='Student Class')
    s_address = forms.CharField(max_length=30,label='Student Address')
    s_school = forms.CharField(max_length=30,label='Student School')
    s_email = forms.EmailField(max_length=30,label='Student E-mail')

class sform(forms.Form):
    s_name = forms.CharField(max_length=30,label='Student Name')

