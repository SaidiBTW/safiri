from django .forms import ModelForm
from .models import Seat

class SeatForm(ModelForm):
    class Meta:
        model =  Seat
        fields = ['seat_number',]