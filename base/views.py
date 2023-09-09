from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import requests
import json
from authentication.models import booking, Taxi

# @login_required
def view(request):
    user_latitude = request.GET.get('lat')
    user_longitude = request.GET.get('lng')

    # Get the closest available taxi
    available_taxis = Taxi.objects.filter(booking__isnull=True)
    closest_taxi = None
    closest_distance = None
    for taxi in available_taxis:
        distance = get_distance(user_latitude, user_longitude, taxi.latitude, taxi.longitude)
        if closest_taxi is None or distance < closest_distance:
            closest_taxi = taxi
            closest_distance = distance

    return render(request, 'base/home.html', {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
        'user_latitude': user_latitude,
        'user_longitude': user_longitude,
        'closest_taxi': closest_taxi,
        'closest_distance': closest_distance,
    })

# @login_required
def book_taxi(request):
    user_latitude = request.GET.get('lat')
    user_longitude = request.GET.get('lng')

    # Get the closest available taxi
    available_taxis = Taxi.objects.filter(booking__isnull=True)
    closest_taxi = None
    closest_distance = None
    for taxi in available_taxis:
        distance = get_distance(user_latitude, user_longitude, taxi.latitude, taxi.longitude)
        if closest_taxi is None or distance < closest_distance:
            closest_taxi = taxi
            closest_distance = distance

    if closest_taxi is None:
        messages.error(request, "Sorry, no taxis are currently available. Please try again later.")
        return redirect('view')

    if request.method == 'POST':
        pickup_time = request.POST.get('pickup_time')
        pickup_location = request.POST.get('pickup_location')
        dropoff_location = request.POST.get('dropoff_location')

        Booking = booking.objects.create(
            user=request.user,
            taxi=closest_taxi,
            status='Pending',
            pickup_time=pickup_time,
            pickup_location=pickup_location,
            dropoff_location=dropoff_location,
        )

        messages.success(request, "Your taxi booking has been submitted. Please wait for confirmation from the admin.")
        return redirect('booking_detail', booking_id=booking.id)

    return render(request, 'bookings/book_taxi.html', {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
        'user_latitude': user_latitude,
        'user_longitude': user_longitude,
        'closest_taxi': closest_taxi,
        'closest_distance': closest_distance,
    })

# @login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(booking, id=booking_id)

    if booking.user != request.user:
        messages.error(request, "Sorry, you do not have permission to view this booking.")
        return redirect('home')

    return render(request, 'bookings/booking_detail.html', {
        'booking': booking,
    })

def get_distance(lat1, lng1, lat2, lng2):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={},{}&destinations={},{}&key={}'.format(lat1, lng1, lat2, lng2, settings.GOOGLE_MAPS_API_KEY)
    response = requests.get(url)
    data = json.loads(response.content)
    return data['rows'][0]['elements'][0]['distance']['value']
