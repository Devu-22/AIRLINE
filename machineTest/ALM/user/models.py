from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model

# Flight Model
class Flight(models.Model):
    flight_id = models.CharField(max_length=10, unique=True)
    dep_airport = models.CharField(max_length=50)
    dep_date = models.DateField()
    dep_time = models.TimeField()
    arr_airport = models.CharField(max_length=50)
    arr_date = models.DateField()
    arr_time = models.TimeField()

    def __str__(self):
        return f"{self.flight_id} - {self.dep_airport} to {self.arr_airport}"
