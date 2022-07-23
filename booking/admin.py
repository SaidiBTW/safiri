from django.contrib import admin
from .models import (
    Route,
    Bus,
    Seat,
    Ticket
)


# Register your models here.
class BusInLine(admin.StackedInline):
    model = Bus
    extra: int = 1
    
class SeatInLine(admin.StackedInline):
    model = Seat
    extra: int = 1

class RouteAdmin(admin.ModelAdmin):
    inlines =[
        BusInLine,
    ]




admin.site.register(Route,RouteAdmin)
admin.site.register(Seat)
admin.site.register(Ticket)