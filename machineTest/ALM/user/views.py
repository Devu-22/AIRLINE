from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Flight
from .forms import FlightForm

# Main page view
def main(request):
    return render(request, 'main.html')

# Admin Registration View
def admin_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Using Django's built-in UserCreationForm
        if form.is_valid():
            form.save()
            return redirect('admin_login')
    else:
        form = UserCreationForm()
    return render(request, 'admin_register.html', {'form': form})

# Admin Login View
def admin_login(request):
    form = AuthenticationForm(request, data=request.POST or None)  # Using Django's built-in AuthenticationForm

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            form.add_error(None, 'Invalid credentials')

    return render(request, 'admin_login.html', {'form': form})

# Admin Logout View
@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required
def admin_dashboard(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'admin_dashboard.html', {'user': user})

# CRUD Operations for Flights
@login_required
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flight_list.html', {'flights': flights})

@login_required
def flight_search(request):
    if request.method == 'POST':
        flight_id = request.POST.get('flight_id')
        flight = Flight.objects.filter(flight_id=flight_id).first()
        return render(request, 'flight_detail.html', {'flight': flight})
    return render(request, 'flight_search.html')

@login_required
def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'add_flight.html', {'form': form})

@login_required
def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight, flight_id=flight_id)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'edit_flight.html', {'form': form})


@login_required
def edit_flight_main(request):
    if request.method == 'POST':
        flight_id = request.POST.get('flight_id')
        if flight_id:
            # Check if the flight with the given ID exists
            flight = Flight.objects.filter(flight_id=flight_id).first()
            if flight:
                return redirect('edit_flight', flight_id=flight_id)
            else:
                return render(request, 'edit_flight_main.html', {'error': 'Flight ID does not exist.'})
    return render(request, 'edit_flight_main.html')