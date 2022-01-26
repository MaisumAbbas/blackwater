from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,"Website/home/index.html")


def services(request):

    return render(request,"Website/our_services/services.html")

def faq(request):

    return render(request,"Website/our_services/faq.html")

def reviews(request):

    return render(request,"Website/our_firm/black_water_reviews.html")


def responsbility(request):

    return render(request,"Website/our_firm/corporate_responsibility.html")



def advanceBlog(request):

    return render(request,"Website/our_firm/credit_advice_block.html")
    

def contactus(request):

    return render(request,"Website/Contact_us/contact_us.html")
    

def credit_companies(request):

    return render(request,"Website/credit_help/credit_companies.html")
    
def free_consulting(request):

    return render(request,"Website/home/free_consulting.html")

def credit_help(request):

    return render(request,"Website/credit_help/credit_help.html")