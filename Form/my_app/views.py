# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from my_app.models import Employee, Company
from . import forms


# Create your views here.
def index(request):
    # return HttpResponse("Hello ......................" )
    employees = Employee.objects.order_by('name')

    form_add_comp = forms.FormAddCompany()
    return render(request, 'my_app/index.html', {'employees': employees, 'form_add_comp': form_add_comp})


def my_check(request):
    form_add_comp = forms.FormAddCompany()
    if request.method == "POST":
        form = forms.FormAddCompany(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('index'))


def about(request):
    return render(request, 'my_app/about.html', {'index': 'about'})


def add_company_form(request):
    form_add_comp = forms.FormAddCompany()
    if request.method == "POST":
        form = forms.FormAddCompany(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # return render(request, 'my_app/index.html', {'form_add_comp': form_add_comp})
            return index(request)

    return render(request, 'my_app/add_company_form.html', {'form_add_comp': form_add_comp})
