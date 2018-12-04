from django import forms
from my_app.models import Company, Employee
from django.core import validators


# class FormAddEmployee(forms.Form):
#     name = forms.CharField(max_length=255)
#     age = forms.IntegerField()
#     phone = forms.IntegerField()
#     email = forms.EmailField()
#     company = forms.


class FormAddCompany(forms.ModelForm):
    # name = forms.CharField(max_length=255)
    # address = forms.CharField(max_length=255)

    class Meta:
        model = Company
        fields = ('name','address')



    #############################################################
    # address = forms.CharField(widget=forms.Textarea)
    # bootcatcher = forms.CharField()
    #
    # def clean_bootcatcher(self):
    #    bootcatcher = self.cleaned_data['bootcatcher']
    #    if len(bootcatcher) > 1:
    #        print ('>1')
    #        raise forms.ValidationError("lenght greater than one")
    #    return bootcatcher
