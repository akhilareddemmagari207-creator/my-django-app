from django.db import models
from django.contrib.auth.models import User
from accounts.models import vendorRegistration

# Board Plan: busTypes Choices List
BUS_TYPES = [
    ('SEMI SLEEPER AC', 'Semi Sleeper AC'),
    ('SEMI SLEEPER NON AC', 'Semi Sleeper non AC'),
    ('SLEEPER NON AC', 'Sleeper non AC'),
    ('SLEEPER AC', 'Sleeper AC'),
]

# Board Plan: class ALLBuses
class ALLBuses(models.Model):
    vendor = models.ForeignKey(vendorRegistration, on_delete=models.CASCADE, related_name='vendorbuses')
    bus_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    bus_type = models.CharField(max_length=100, choices=BUS_TYPES)
    starting = models.CharField(max_length=100)
    endpoint = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.IntegerField()
    total_seats = models.IntegerField()
    amenities = models.TextField()
    
    # class Meta:
    #     verbose_name_plural = "ALL Buses"

    # def __str__(self):
    #     return f"{self.bus_name} - {self.company}"
