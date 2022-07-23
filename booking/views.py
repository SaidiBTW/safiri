from typing import List
from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from .models import Route,Bus, Seat,Ticket
from .forms import SeatForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def route_list_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    routes = Route.objects.filter(start_point__icontains = q)
    context = {'routes':routes}

    return render(request,'route_list.html',context)


def seat_create_view(request, pk):
    bus = Bus.objects.get(id=pk)
    form  = SeatForm()

    if(request.method == 'POST'):
        form = SeatForm(request.POST)
        if form.is_valid():
            #use flash messages to show if seat is taken
            seat = Seat.objects.create(
                bus = bus,
                seat_number = request.POST.get('seat_number'),
                is_taken = True
            )
            Ticket.objects.create(
                owner = request.user,
                seat = seat,
            )
            
            
            return redirect('myticket')
    
    context = {'bus': bus,'form':form}
    return render(request,'seat_selection.html',context)

def ticket_view(request):
    ticket = Ticket.objects.get(owner = request.user)
    context = {'ticket':ticket}

    return render(request,'ticket_detail.html',context)

