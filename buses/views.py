from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BusCreationForm
from .models import ALLBuses
from accounts.models import vendorRegistration

@login_required(login_url='login')
def add_bus(request):
    if request.method == 'POST':
        form = BusCreationForm(request.POST)
        if form.is_valid():
            bus = form.save(commit=False)
            bus.vendor = vendorRegistration.objects.get(user=request.user)
            bus.save()
            return redirect('vendor_dashboard')
    else:
        form = BusCreationForm()
    return render(request, 'buses/add_bus.html', {'form': form})

def bus_seat_layout(request, bus_id):
    bus = ALLBuses.objects.get(id=bus_id)
    lower_rows = range(1, 6)
    upper_rows = range(6, 11)
    return render(request, "buses/bus_seat_layout.html", {'bus': bus, 'lower_rows': lower_rows, 'upper_rows': upper_rows})
