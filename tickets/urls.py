from django.urls import path
from .views import (
    TicketListView,
    TicketCreateView,
    TicketUpdateView,
    TicketDeleteView
)
app_name = "tickets"

urlpatterns = [
    path("", TicketListView.as_view(), name="ticket_list"),
    path("nuevo/", TicketCreateView.as_view(), name="ticket_create"),
    path("editar/<int:pk>/", TicketUpdateView.as_view(), name="ticket_update"),
    path("eliminar/<int:pk>/", TicketDeleteView.as_view(), name="ticket_delete"),
]