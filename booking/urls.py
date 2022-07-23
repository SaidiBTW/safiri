from django.urls import path
from .views import route_list_view,seat_create_view,ticket_view

urlpatterns = [
    path('',route_list_view,name='route_list'),
    path('<int:pk>/seatselect/',seat_create_view, name='seat_select'),
    path('myticket/',ticket_view,name='myticket')
    
]