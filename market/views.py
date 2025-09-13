from django.shortcuts import render, get_object_or_404, redirect
from .models import Bike, Brand
from .forms import BikeForm, ContactForm, BookingForm
from django.db.models import Q

def index(request):
    bikes = Bike.objects.all()
    return render(request, 'index.html', {'bikes': bikes})

def about(request):
    return render(request, 'aboutus.html')

def buy_list(request):
    qs = Bike.objects.filter(is_booked=False).order_by('-created_at')
    # basic filters via GET
    brand = request.GET.get('brand')
    q = request.GET.get('q')
    year = request.GET.get('year')
    sort = request.GET.get('sort')
    if brand:
        qs = qs.filter(brand__name__iexact=brand)
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(model__icontains=q) | Q(description__icontains=q))
    if year:
        try:
            qs = qs.filter(year=int(year))
        except:
            pass
    if sort == 'price_asc':
        qs = qs.order_by('price')
    elif sort == 'price_desc':
        qs = qs.order_by('-price')

    brands = Brand.objects.all()
    return render(request, 'buy.html', {'bikes': qs, 'brands': brands})

def buy1(request):
    return render(request, 'buy1.html')

def sell_bike(request):
    if request.method == 'POST':
        form = BikeForm(request.POST, request.FILES)
        if form.is_valid():
            bike = form.save()
            return redirect('market:bike_detail', pk=bike.pk)
    else:
        form = BikeForm()
    return render(request, 'sell.html', {'form': form})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contactus.html', {'success': True})
    else:
        form = ContactForm()
    return render(request, 'contactus.html', {'form': form})

def pay(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    if request.method == 'POST':
        # simulate payment -> create booking
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            booking.status = 'paid'
            booking.save()
            # mark bike booked
            bike.is_booked = True
            bike.save()
            return redirect('market:booking_confirmation', pk=booking.pk)
    else:
        form = BookingForm(initial={'bike': bike.pk, 'amount': bike.price})
    return render(request, 'pay.html', {'bike': bike, 'form': form})

def booking_confirmation(request, pk):
    from .models import Booking
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking_confirmation.html', {'booking': booking})
