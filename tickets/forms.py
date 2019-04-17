from django import forms
from .models import Ticket
from django.contrib.auth.models import User  # Required to assign User as a submitter


class RawTicketForm(forms.Form):
    title = forms.CharField()
    summary = forms.CharField()
    urgency = forms.CharField()
    