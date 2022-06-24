"""djangoProject622 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_student),
    path('add_cls/', add_view_cls),
    path('add_tea/', add_view_tea),
    path('add_stu/', add_view_stu),
    path('delete_cls/<int:id>', delete_view_cls),
    path('delete_tea/<int:id>', delete_view_tea),
    path('delete_stu/<int:id>', delete_view_stu),
    path('update_tea/<int:id>', update_view_tea),
    path('update_cls/<int:id>', update_view_cls),
    path('update_stu/<int:id>', update_view_stu),
]

