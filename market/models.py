from django.db import models
from django.urls import reverse

class Brand(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)

    def __str__(self):
        return self.name

class Bike(models.Model):
    title = models.CharField(max_length=240)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    model = models.CharField(max_length=120, blank=True)
    variant = models.CharField(max_length=120, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    km_driven = models.PositiveIntegerField(default=0)
    owners = models.PositiveSmallIntegerField(default=1)
    fuel_type = models.CharField(max_length=30, choices=(('Petrol','Petrol'),('Diesel','Diesel'),('Electric','Electric')), default='Petrol')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='bikes/', null=True, blank=True)
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('market:bike_detail', args=[self.pk])

    def __str__(self):
        return f"{self.year} | {self.brand or ''} {self.model or ''} | ₹{self.price}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    reason = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.reason}"

class Booking(models.Model):
    STATUS_CHOICES = (('pending','Pending'),('paid','Paid'),('cancelled','Cancelled'))
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.pk} - {self.bike} - {self.status}"

