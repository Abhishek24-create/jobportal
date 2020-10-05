from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from Webapp.models import adminlogin, Job_Postings, register, Applied_Jobs
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from datetime import datetime
# Create your views here.

def AdminLogin(request):
    username = request.POST.get('name')
    password = request.POST.get('password')
    #
    # adminlogin(username=username,password=password).save()
    # return render(request,"admin.html")
    qs = adminlogin.objects.filter(username=username,password=password)
    if qs:
        return render(request,"MyApp/home.html")
    else:
        return render(request,"MyApp/admin.html",{'message':'Invalid User'})

def Base_Page(request):
        return render(request,'MyApp/base.html')

#
# def Home_Page(request):
#     # if request.sessions.has_key('is_logged'):
#
#         return render(request,'MyApp/home.html')
#     # return redirect('register')
#
def Login(request):

    if request.POST:
        useremail= request.POST.get('email')
        password = request.POST.get('password')
        select = request.POST.get("select")
        count = register.objects.filter(email=useremail,password=password,select=select)
        if count.count()>0:
            request.session['useremail'] = useremail
            request.session['type'] = select
            # request.session['id'] = count.id
            return redirect("/", {'useremail':useremail, 'type':select})
        else:
            return render(request,"MyApp/login.html",{'message':'Invalid User or Password'})


def Logout(request):
      request.session.flush()
      return redirect("/")

def Register(request):
    return render(request,"MyApp/registration.html")

def Search_Jobs(request):
    position = request.POST.get('position')
    location = request.POST.get('location')
    search = Job_Postings.objects.filter(vacancyname=position, city=location)
    if search.count() > 0:
        return render(request,"MyApp/search.html",{'search':search})
    else:
        return render(request, "MyApp/search.html", {'messages':'Invalid Search'})

def Job_Details(request):
    id = request.POST.get('jobid')
    appliedby = request.session['useremail']
    detail = Job_Postings.objects.filter(id=id)
    if('useremail' in request.session):
        selects = Applied_Jobs.objects.filter(appliedby = appliedby, appliedfor = id, status = 'Applied')
    if selects.count() > 0:
        contex = {'selects':'Yes', 'detail':detail}
        return render(request,"MyApp/jobdetails.html", contex)
    else:
        return render(request, "MyApp/jobdetails.html", {'detail':detail})



def SaveRegister(request):
    username = request.POST.get("a1")
    # dob = None
    email = request.POST.get("a3")
    # gender = None
    # mob = None
    # qualification = None
    # address = None
    select = request.POST.get("a8")
    password = request.POST.get("a10")
    # resume = request.POST.get("a11")
    auth=register.objects.filter(email=email).count()
    if auth>0:
        message="User Already Registered With This User"
        return render(request, "MyApp/registration.html", {'message': message})
    else:
        register(username=username, email=email, select=select, password=password).save()
    return render(request, "MyApp/login.html")


def PostSaved(request):
    companyname = request.POST.get('company')
    country= request.POST.get('country')
    pincode = request.POST.get('pincode')
    city = request.POST.get('city')
    state = request.POST.get('state')
    address = request.POST.get('address')
    vacancyname = request.POST.get('vacancy_name')
    vacancytype = request.POST.get('vacancy_type')
    salary = request.POST.get('salary')
    qualification = request.POST.get('req_qlf')
    aboutjob = request.POST.get('particulars')
    postedby = request.POST.get(request.session['useremail'])
    vacancy = request.POST.get('vacancy')
    Job_Postings(companyname=companyname,country=country,pincode=pincode,city=city,state=state,
                 qualification=qualification, address=address,vacancyname=vacancyname,vacancytype=vacancytype,salary=salary,
                 aboutjob=aboutjob, postedby=postedby,vacancy=vacancy).save()
    return render(request,"MyApp/portal.html",{'message':'Posted Successfully'})

def ViewJobs(request):
   show = Job_Postings.objects.all()
   context = {'show':show}
   # today = datetime.now()
   return render(request, 'MyApp/home.html', context)

def PostedJobs(request):
   show = Job_Postings.objects.filter(postedby=request.session['useremail'])
   context = {'show':show}
   return render(request, 'MyApp/postedjobs.html', context)


def Edit_Job(request):
    id = request.POST.get('jobid')
    edit = Job_Postings.objects.filter(id=id)
    return render(request,"MyApp/editjob.html", {'edit':edit})


def Update(request):
    id = request.POST.get('jobid')
    companyname = request.POST.get('company')
    country = request.POST.get('country')
    pincode = request.POST.get('pincode')
    city = request.POST.get('city')
    state = request.POST.get('state')
    address = request.POST.get('address')
    vacancyname = request.POST.get('vacancy_name')
    vacancytype = request.POST.get('vacancy_type')
    salary = request.POST.get('salary')
    qualification = request.POST.get('req_qlf')
    aboutjob = request.POST.get('particulars')
    vacancy = request.POST.get('vacancy')
    update = Job_Postings.objects.filter(id=id).update(companyname=companyname, country=country, pincode=pincode, city=city, state=state,
             qualification=qualification, address=address, vacancyname=vacancyname, vacancytype=vacancytype,
             salary=salary,
             aboutjob=aboutjob, vacancy=vacancy)
    if update:
        edit = Job_Postings.objects.filter(id=id)
        return render(request, "MyApp/editjob.html", {'message': 'Update Successfully', 'edit':edit})
    else:
        return render(request, "MyApp/editjob.html", {'message': 'Not Updated'})

def Change_password(request):
    pwd = request.POST.get('pwd')
    cnf_pwd = request.POST.get('cnf_pwd')
    if pwd != cnf_pwd:
        return redirect('/', {'messages': 'Password Did Not Match'})
    else:
        change = register.objects.filter(email=request.session['useremail']).update(password=cnf_pwd)
        if change:
            return  redirect('/',{'messages':'Updated Successfully' })
        else:
            return  redirect('/',{'messages':'Not Updated'})


def Apply(request):
    appliedby = request.session['useremail']
    appliedfor = request.POST.get('jobid')
    datee = datetime.now()
    appliedon = datee.strftime("%Y-%m-%d %H:%M:%S")
    status = 'Applied'
    detail = Job_Postings.objects.filter(id=appliedfor)
    selects = Applied_Jobs.objects.filter(appliedby=request.session['useremail'], appliedfor=appliedfor,
                                          status='Applied')
    if selects.count() > 0:
        context = {'message': 'Already Applied', 'detail':detail, 'selects':'Yes'}
        return render(request, 'MyApp/jobdetails.html', context)
    else:
        Applied_Jobs(appliedby=appliedby, appliedfor=appliedfor, appliedon=appliedon, status=status).save()
        return render(request,'MyApp/jobdetails.html',{'message':'Applied Successfully','detail':detail})


def Applied_View(request):
    view = Applied_Jobs.objects.filter(appliedby=request.session['useremail'])
    for id in view:
        jobsview = Job_Postings.objects.get(id=id.appliedfor)

    data = {
        "views": view
    }
    return render(request, 'MyApp/appliedjobs.html', {'data': data, 'jobsview': jobsview})
    view = Applied_Jobs.objects.filter(appliedby=request.session['useremail'])
    # view = Saved_Jobs.objects.filter(appliedby=request.session['useremail'])
    # if view.count() > 0:
    #     for id in view:
    #         jobsview = Job_Postings.objects.filter(id = id.appliedfor)
    #         return render(request, 'MyApp/appliedjobs.html', {'jobsview': jobsview, 'view': view})
    # else:
    #     return render(request, 'MyApp/appliedjobs.html', {'messsage': 'No data found'})


# def ViewJobs(request):
#     show=register.objects.all
#     context={'show':show}
#     return render(request, 'MyApp/registration.html',context)
#
# def Regd(request):
#     username = request.POST.get('name')
#     password = request.POST.get('password')
#     show=register.objects.get(username=username, password=password)
#     context={'show':show}
#     return render(request, 'MyApp/timetable.html',context)
#
