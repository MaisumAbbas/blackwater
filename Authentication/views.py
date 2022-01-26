import email
from django.http import request
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.http import HttpResponse , HttpResponseRedirect

from Authentication.models import user_detail,providerdetail
# Create your views here.


def check_user(request):
    if request.method =="GET":
        un = request.GET["user_n"]
        check = User.objects.filter(email=un)

        if len(check)==1:
            return HttpResponse("Exists")
        else :
            return HttpResponse ("Not Exists")
        print (check,len(check))
        print (un)
    return HttpResponse("Hello")

def login(request):
    if request.method == 'POST':
        print ("in sign in post")
        un =  request.POST["name"]
        pass1 =  request.POST["password"]
        user= authenticate(username=un,password=pass1)
        if user is not None:
            return HttpResponseRedirect('/')
        else:
            return render(request,"Authentication/login.html",{'context':"Error in username or password"})

    return render(request,"Authentication/login.html")

def register(request):

    if request.method == 'POST':
        print ("in post")
        firtname=request.POST['firtname']
        midlename=request.POST['midlename']

        midlename1=request.POST['midlename']

        lastname=request.POST['lastname']
        suffix=request.POST['suffix']
        email=request.POST['email']
        password=request.POST['password']
        snn_number=request.POST['snn_number']
        dob=request.POST['dob']
        phone_h=request.POST['phone_h']
        phone_w=request.POST['phone_w']
        phone_M=request.POST['phone_M']
        fax=request.POST['fax']
        mail_address=request.POST['mail_address']
        city=request.POST['city']
        state=request.POST['state']
        zip_code=request.POST['zip_code']
        country=request.POST['country']

        p_detail=request.POST['p_detail']
        username=request.POST['username']
        password2=request.POST['password2']
        num=request.POST['num']
        note=request.POST['note']


        #user created
        usr = User.objects.create_user(email,email,password)
        usr.first_name = firtname
        usr.last_name =lastname
        usr.save()

        #additional detail
        detail = user_detail(user=usr,midelname=midlename,suffix=suffix,last_snn=snn_number,dob=dob,phone_h=phone_h,phone_w=phone_w,phone_m=phone_M,fax=fax,mail_address=mail_address,city=city,state=state,zipcode=zip_code)
        detail.save()

        #provider detail
        provider = providerdetail(user=usr,p_detail=p_detail,username=username,password2=password2,num=num,note=note)
        provider.save()


        print (request.POST)
        print (firtname)
        print (country)

        # user = user_detail.objects.create(firstname=firtname,last_snn=snn_number,dob=dob)
        # user.save()
        # print (fname)


    return render(request,"Authentication/register.html")