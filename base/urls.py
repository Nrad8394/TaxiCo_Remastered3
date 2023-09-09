from django.urls import path
from base import views

urlpatterns = [
    path('view/', views.view, name='view'),
    path('book_taxi/', views.book_taxi, name='book_taxi'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('signup', views.book_taxi, name='signup'),
]
