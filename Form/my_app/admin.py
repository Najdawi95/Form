# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from my_app.models import Employee, Company

# Register your models here.
admin.site.register(Employee)
admin.site.register(Company)