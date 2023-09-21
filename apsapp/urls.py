from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('apsregistration',views.apsregistration,name="apsregistration"),
    path('payment', views.payment, name="payment"),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback/thankyou/', views.feedback_thankyou, name='feedback_thankyou'),
    path('contact', views.contact, name="contact"),
    path('apslogin',views.apslogin,name="apslogin"),
    path('checkapslogin',views.checkapslogin,name="checkapslogin"),
    path('apshome',views.apshome,name="apshome"),
    path('apsprofile',views.apsprofile,name="apsprofile"),
    path('apschangepwd',views.apschangepwd,name="apschangepwd"),
    path('apsupdatepwd', views.apsupdatepwd, name="apsupdatepwd"),
    path("viewezodiacsigns",views.viewezodiacsigns,name="viewezodiacsigns"),
    path("displayzodiacsigns",views.displayzodiacsigns,name="displayzodiacsigns"),
    path('apslogout',views.apslogout,name='apslogout'),

    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('checkadminlogin',views.checkadminlogin,name="checkadminlogin"),
    path('adminhome',views.adminhome,name="adminhome"),
    path("addzodiac",views.addzodiac,name="addzodiac"),
    path("viewazodiacsigns",views.viewazodiacsigns,name="viewazodiacsigns"),
    path('viewcustomers',views.viewcustomers,name="viewcustomers"),
    path("deleteaps/<int:aid>",views.deleteaps,name="deleteaps"),
    path('adminlogout', views.adminlogout, name='adminlogout'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

