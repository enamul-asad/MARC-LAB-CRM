from django.urls import path
from . import views

urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('logout/',views.logout,name="logout"),
    path('viewcustomers/',views.viewcustomers,name="viewcustomers"),
    path('viewenquiries/',views.viewenquiries,name="viewenquiries"),
    path('delenq/<id>',views.delenq,name="delenq"),
    path('product/',views.product,name="product"),
    path('viewcomplaints/',views.viewcomplaints,name="viewcomplaints"),
    path('delcomp/<id>',views.delcomp,name="delcomp"),
    path('viewfeedbacks/',views.viewfeedbacks,name="viewfeedbacks"),
    path('delfeed/<id>',views.delfeed,name="delfeed"),
    path('changepassword/',views.changepassword,name="changepassword"),


]