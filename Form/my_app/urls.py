from django.conf.urls import url
from my_app import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^index', views.index, name="index"),
    url(r'^about', views.about, name="about"),
    url(r'^form', views.add_company_form, name="form"),
    url(r'^my_check', views.my_check, name="my_check"),
]

