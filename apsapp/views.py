from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm,ZodiacsignForm,AdminLoginForm,FeedbackForm
from .models import Customer,Admin,Zodiacsign


def index(request):
    return render(request,"index.html")

def apsregistration(request):
    form = CustomerRegistrationForm()
    if request.method == "POST":
        formdata = CustomerRegistrationForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg="Customer Registered Successfully"
            return render(request, "apsregistration.html", {"apsform": form,"msg":msg})
        else:
            msg = "Failed to Register Customer"
            return render(request, "apsregistration.html", {"apsform": form, "msg": msg})
    return render(request,"apsregistration.html",{"apsform":form})
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_thankyou')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_thankyou(request):
    return render(request, 'feedback_thankyou.html')

def apslogin(request):
    return render(request,"apslogin.html")
def contact(request):
    return render(request,"contact.html")

def payment(request):
    return render(request,"payment.html")


def checkapslogin(request):
    uname = request.POST.get("ausername")
    pwd = request.POST.get("apassword")

    flag = Customer.objects.filter(Q(username=uname) & Q(password=pwd))

    print(flag)

    if flag:
        aps = Customer.objects.get(username=uname)
        print(aps)
        request.session["aid"] = aps.id
        request.session["aname"] = aps.fullname
        return render(request, "apshome.html", {"aid": aps.id, "aname": aps.fullname})
    else:
        msg = "Login Failed"
        return render(request, "apslogin.html", {"msg": msg})


def apshome(request):
    aid=request.session["aid"]
    aname=request.session["aname"]

    return render(request,"apshome.html",{"aid":aid,"aname":aname})

def apsprofile(request):
    aid=request.session["aid"]
    aname=request.session["aname"]
    aps = Customer.objects.get(id=aid)
    return render(request,"apsprofile.html",{"aid":aid,"aname":aname,"aps":aps})

def apschangepwd(request):
    aid=request.session["aid"]
    aname=request.session["aname"]
    return render(request,"apschangepwd.html",{"aid":aid,"ename":aname})

def apsupdatepwd(request):
    aid=request.session["aid"]
    aname=request.session["aname"]

    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]

    flag = Customer.objects.filter(Q(id=aid) & Q(password=opwd))

    if flag:
        Customer.objects.filter(id=aid).update(password=npwd)
        msg = "Password Updated Successfully"
        return render(request, "apschangepwd.html", {"eid": aid, "ename": aname,"msg":msg})
    else:
        msg = "Old Password is Incorrect"
        return render(request, "apschangepwd.html", {"eid": aid, "ename": aname,"msg":msg})

def viewezodiacsigns(request):

    aid=request.session["aid"]
    aname=request.session["aname"]

    zodiaclist = Zodiacsign.objects.all()

    return render(request,"viewezodiacsigns.html",{"aid": aid, "ename": aname,"zodiaclist":zodiaclist})

def displayzodiacsigns(request):

    aid=request.session["aid"]
    aname=request.session["aname"]

    pname = request.POST["pname"]
    print(pname)

    zodiaclist = Zodiacsign.objects.filter(name__icontains=pname)

    return render(request,"displayzodiacsigns.html",{"eid": aid, "ename": aname,"zodiaclist":zodiaclist})


def apslogout(request):
    return render(request,"apslogin.html")

def adminlogin(request):
    return render(request,"adminlogin.html")

def checkadminlogin(request):
    print("welcome1")
    uname = request.POST.get("ausername")
    pwd = request.POST.get("apassword")

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        request.session["auname"] = admin.username
        return render(request, "adminhome.html", {"auname": admin.username})
    else:
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})


def adminhome(request):
    auname=request.session["auname"]
    return render(request,"adminhome.html",{"auname":auname})



def addzodiac(request):
    auname = request.session["auname"]
    form = ZodiacsignForm()
    if request.method == "POST":
        formdata = ZodiacsignForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Zodiac Sign Added Successfully"
            return render(request, "addzodiac.html", {"auname":auname,"productform": form,"msg":msg})
        else:
            msg = "Failed to Add Zodiac"
            return render(request, "addzodiac.html", {"auname":auname,"productform": form, "msg": msg})
    return render(request,"addzodiac.html",{"auname":auname,"zodiacform":form})

def viewcustomers(request):
    auname=request.session["auname"]
    apslist = Customer.objects.all()
    count = Customer.objects.count()
    return render(request,"viewcustomers.html",{"auname":auname,"apslist":apslist,"count":count})



def viewazodiacsigns(request):
    auname=request.session["auname"]
    zodiaclist = Zodiacsign.objects.all()
    count = Zodiacsign.objects.count()
    return render(request,"viewazodiacsigns.html",{"auname":auname,"zodiaclist":zodiaclist,"count":count})

def deleteaps(request,aid):
    Zodiacsign.objects.filter(id=aid).delete()
    return redirect("viewcustomers.html")

def adminlogout(request):
    return render(request,"adminlogin.html")