from django.shortcuts import render, redirect
from crmapp.models import Customer, Login
from django.views.decorators.cache import cache_control
import datetime
from . models import Response
from adminapp.models import Product
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def customerhome(request):
    try:
        if request.session["userid"]!=None:
            userid=request.session["userid"]
            cust=Customer.objects.get(emailaddress=userid)
            return render(request,"customerhome.html", locals())
    except KeyError:
        return redirect("crmapp:login")
    
def logout(request):
    try:
        del request.session["userid"]
    except KeyError:
        return redirect("crmapp:login")
    return redirect("crmapp:login")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def response(request):
    try:
        if request.session['userid']!=None:
            cust=Customer.objects.get(emailaddress=request.session['userid'])
            if request.method=="POST":
                name = cust.name
                contactno = cust.contactno
                emailaddress = cust.emailaddress
                responsetype = request.POST['responsetype']
                subject = request.POST['subject']
                responsetext = request.POST['responsetext']
                posteddate = datetime.datetime.today()
                res = Response(name=name, contactno=contactno, emailaddress=emailaddress, responsetype=responsetype, subject=subject, responsetext=responsetext, posteddate=posteddate)
                res.save()
                msg="Your response has been send successfully"
                return render(request,"response.html",{"msg":msg})
            return render(request,"response.html")
    except KeyError:
         return redirect("crmapp:login")
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewprofile(request):
    try:
        if request.session["userid"]!=None:
            userid=request.session["userid"]
            cust=Customer.objects.get(emailaddress=userid)
            if request.method=="POST":
                name=request.POST["name"]
                gender=request.POST["gender"]
                address=request.POST["address"]
                contactno=request.POST["contactno"]
                emailaddress=request.POST["emailaddress"]
                Customer.objects.filter(emailaddress=emailaddress).update(name=name,gender=gender,address=address,contactno=contactno)
                return redirect("customerapp:customerhome")
            return render(request,"viewprofile.html", locals())
    except KeyError:
        return redirect("crmapp:login")
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def products(request):
    try:
        if request.session["userid"]!=None:
            userid=request.session["userid"]
            cust=Customer.objects.get(emailaddress=userid)
            prod=Product.objects.all
            return render(request,"products.html", locals())
    except KeyError:
        return redirect("crmapp:login")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def changepassword(request):
    try:
        if request.session["userid"]!=None:
            userid=request.session["userid"]
            if request.method=="POST":
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                cnfpassword=request.POST['cnfpassword']
                obj = Login.objects.get(userid=userid)
                if newpassword != cnfpassword:
                    msg = "New Password and Confirm are not matched"
                elif obj.password != oldpassword:
                    msg = "Invalid old Password"
                elif obj.password==oldpassword:
                    Login.objects.filter(userid=userid,password=oldpassword).update(password=newpassword)
                    return redirect("crmapp:login")
                return render(request, "changepassword.html",locals())
            return render(request,"changepassword.html", locals())
    except KeyError:
        return redirect("crmapp:login")
