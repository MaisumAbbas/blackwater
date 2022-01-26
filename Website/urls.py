"""Blackwater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from Website import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('our_services/services/',views.services,name="Services"),
    path('our_services/faq/',views.faq,name="Faq"),
    path('our_firm/black_water_reviews/',views.reviews,name="Reviews"),
    path('our_firm/corporate_responsibility/',views.responsbility,name="Responsbility"),
    path('our_firm/credit_advice_block/',views.advanceBlog,name="AdvanceBlog"),
    path('contactus/',views.contactus,name="ContactUs"),
    path('admin/', admin.site.urls),

    path('credit_help/',views.credit_help,name="CreditHelp"),
    path('credit_help/CreditCompanies/',views.credit_companies,name="CreditCompanies"),
    path('free_consulting/',views.free_consulting,name="FreeConsulting"),
]
