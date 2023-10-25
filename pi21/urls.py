"""
URL configuration for pi21 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView
import json

fail=open("./bd.json")
data=json.load(fail)
fail.close()



class indexview(TemplateView):
    template_name = "index.html"



class teacherview(TemplateView):
    template_name="teacher.html"
    extra_context=data


class courses(TemplateView):
    template_name="courses.html"
    extra_context=data

class about(TemplateView):
    template_name="about.html"
    extra_context=data




urlpatterns = [
    path('',indexview.as_view()),
    path('teacher/',teacherview.as_view()),
    path('courses/',courses.as_view()),
    path('about/', about.as_view()),
    path('admin/', admin.site.urls),
]
