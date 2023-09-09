from django.urls import path
from authentication.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/', customloginview.as_view(),name='login'),
    path('register/', registerpage.as_view(),name='register'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('',index,name='index'),
    
    path('list/',bookinglist.as_view(),name='list'),
    path('create/',bookingcreate.as_view(),name='create'),
    path('detail/<int:pk>/',bookingdetail.as_view(),name='detail'),
    path('update/<int:pk>/',bookingupdate.as_view(),name='update'),
    path('delete/<int:pk>/',bookingdelete.as_view(),name='delete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



