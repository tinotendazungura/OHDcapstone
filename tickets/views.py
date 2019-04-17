from django.shortcuts import render
from .models import Ticket
from django.shortcuts import render, get_object_or_404, redirect

import datetime
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RawTicketForm


# Create your views here.

@login_required
def home_view(request):
    return render(request, "index.html", {})

def landing_view(request):
    return render(request, "landing.html", {})

def login_view(request):
    return render(request, "login.html", {})



@login_required
def ticket_list_view(request):
    queryset = Ticket.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

class TicketByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing tickets created by current user."""
    model = Ticket
    template_name = 'tickets/ticket_list_created_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter(submitter=self.request.user).filter(status__exact='O').order_by('date_created')


class TicketListView(generic.ListView):
    model=Ticket

class TicketDetailView(LoginRequiredMixin, generic.DetailView):
    template_name='tickets/ticket_detail.html'
    queryset = Ticket.objects.all()


@login_required
def ticket_create_view(request):
    my_form = RawTicketForm()
    if request.method == "POST":
        my_form = RawTicketForm(request.POST)
        if my_form.is_valid():
            #validation built into Django that hands over cleaned data
            Ticket.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form":my_form
    }
    return render(request, "tickets/ticket_create.html", context)