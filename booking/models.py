from django.db import models
from django.urls import reverse

# Create your models here.

class Route(models.Model):
    start_point = models.CharField( max_length=50)
    end_point = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.start_point} -> {self.end_point}'


class Bus(models.Model):
    class Meta:
        ordering = ['departure']
    number_plate = models.CharField(max_length=8)
    route = models.ForeignKey(
        to=Route,
        on_delete=models.CASCADE,
        related_name='buses')
    departure = models.DateTimeField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.number_plate
    
    def get_absolute_url(self):
        return reverse('route_list')

class Seat(models.Model):
    SEAT_CHOICES_PSV = (
        ('1','1'),
        ('2','2')
    )

    seat_number = models.CharField(
        choices = SEAT_CHOICES_PSV,
        max_length=2
    )
    is_taken = models.BooleanField(default=False)
    bus = models.ForeignKey(
        to=Bus,
        on_delete=models.CASCADE,
        related_name='seats'
        )
    
    def __str__(self):
        return f'{self.bus.number_plate} -> Seat : {self.seat_number}'
    
    def get_absolute_url(self):
        return reverse('route_list')
    
class Ticket(models.Model):
    created = models.DateTimeField( auto_now_add=True)
    owner = models.ForeignKey(to = 'accounts.CustomUser',on_delete=models.CASCADE)
    seat = models.ForeignKey(to=Seat,on_delete=models.CASCADE)

    def __str__(self):
        return f'Ticket for {self.owner}'