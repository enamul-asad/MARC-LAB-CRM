from django.urls import path
from . import views

urlpatterns=[
    path('customerhome/',views.customerhome,name="customerhome"),
    path('logout/',views.logout,name="logout"),
    path('response/',views.response,name="response"),
    path('viewprofile/',views.viewprofile,name="viewprofile"),
    path('products/',views.products,name="products"),
    path('changepassword/',views.changepassword,name="changepassword"),

]