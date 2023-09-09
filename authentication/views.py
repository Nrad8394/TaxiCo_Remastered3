import requests
from django import forms
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render,redirect
from .models import *
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import requests
from django import forms
from django.core.exceptions import ValidationError


# Create your views here.
# user authorization operations
def index(requests):
    return render(requests,'authentication/index.html') 
class customloginview(LoginView):
    template_name = 'authentication/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('create')

class registerpage(FormView):
    template_name = 'authentication/register.html'
    form_class = UserCreationForm
    redirect_authenticated = True
    success_url = reverse_lazy('create')
    
    def form_valid(self,form):
        user = form.save()
        
        if user is not None:
            login(self.request,user)
        return super(registerpage,self).form_valid(form)   

# CRUD operations
class  bookingdetail(LoginRequiredMixin,DetailView) :
    model =  booking 
    context_object_name = 'ticket_detail'
    template_name = 'authentication/ticket_detail.html'
    
class bookinglist(LoginRequiredMixin,ListView):
    model = booking 
    context_object_name = "tickets"
    template_name = 'authentication/booking_list.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tickets']= context['tickets'].filter(user=self.request.user)
        # context['count'] = context['tickets'].filter(complete=False).count()    
          
        return context
class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['pickup_location', 'dropoff_location', 'pickup_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
    def clean_pickup_location(self):
        location = self.cleaned_data['pickup_location']
        if not is_location_in_kenya(location):
            raise ValidationError('Location must be in Kenya.')
        return location

    def clean_dropoff_location(self):
        location = self.cleaned_data['dropoff_location']
        if not is_location_in_kenya(location):
            raise ValidationError('Location must be in Kenya.')
        return location

def is_location_in_kenya(location):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key=AIzaSyBTUOh5dOuO1ChgJWkyVjM3KXFtKpzzjyQ'
    response = requests.get(url).json()
    if response['status'] == 'OK':
        for component in response['results'][0]['address_components']:
            if 'country' in component['types'] and component['short_name'] == 'KE':
                return True
    return False


class bookingcreate(LoginRequiredMixin, CreateView):
    model = booking
    form_class = BookingForm  # use custom form
    success_url = reverse_lazy('create')
    template_name = 'authentication/booking_create_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(bookingcreate, self).form_valid(form)
         
        

class  bookingupdate(LoginRequiredMixin,UpdateView):
    model =  booking
    context_object_name = "ticket"
    fields = ['pickup_location','dropoff_location','date','time']
    success_url = reverse_lazy('list')
    template_name = 'authentication/booking_update_form.html'
class  bookingdelete(LoginRequiredMixin,DeleteView):
    model =  booking
    context_object_name = 'ticket'
    success_url = reverse_lazy('list')
    template_name = 'authentication/booking_delete_form.html'
    
  
