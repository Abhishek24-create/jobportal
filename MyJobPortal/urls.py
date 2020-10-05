"""MyJobPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView, ListView
from django.conf import settings
from Webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',TemplateView.as_view(template_name="MyApp/home.html")),
    # path('home/',views.Home_Page),

    path('adminlogin/', TemplateView.as_view(template_name="MyApp/admin.html")),
    path('adminlog/', views.AdminLogin),

    path('logout/',views.Logout),
    path('applicant/', TemplateView.as_view(template_name="MyApp/login.html")),
    path('login/',views.Login),
    path('register/',views.Register),
    path('saveregister/',views.SaveRegister),

    path('job/',TemplateView.as_view(template_name="MyApp/portal.html")),
    path('postsaved/',views.PostSaved),
    path('',views.ViewJobs),

    path('jobdetail/',views.Job_Details),
    path('editjob/',views.Edit_Job),
    path('updatejob/',views.Update),
    path('postedjobs/',views.PostedJobs),
    path('ch_pwd/',views.Change_password),

    path('applied/',views.Apply),
    path('jobsview/',views.Applied_View),
    path('searchjob/',views.Search_Jobs),

    # path('reg/',views.Regd),

]
#