from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
]
# birdsland/urls.py

from django.conf.urls import url
from birdsland import views

# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead

