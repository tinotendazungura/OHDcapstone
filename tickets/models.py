from django.db import models
from django.urls import reverse
import uuid
from django.utils import timezone
from django.contrib.auth.models import User  # Required to assign User as a submitter
import uuid  # Required for unique book instances
from datetime import date

# Create your models here.
class Department(models.Model):
    """Model representing a ticket department."""
    name = models.CharField(max_length=200, help_text='Enter a University department (e.g. ICT)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Ticket(models.Model):
    """Model representing a ticket (but not a specific copy of a ticket)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because ticket can only have one author, but authors can have multiple tickets
    # Author as a string rather than object because it hasn't been declared yet in the file
    #author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    submitter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the ticket')

    URGENCY_LEVEL = (
        ('TP', 'Top Priority'),
        ('NP', 'Normal Priority'),
        ('LP', 'Low Priority'),
    )
    urgency = models.CharField(
        max_length=2,
        choices=URGENCY_LEVEL,
        blank=True,
        default='NP',
        help_text='Ticket Priority',
    )
    # ManyToManyField used because department can contain many tickets. Tickets can cover many departments.
    # Department class has already been defined so we can specify the object above.
    department = models.ManyToManyField(Department, help_text='Select a department for this ticket')

    TICKET_STATUS = (
        ('O', 'Open'),
        ('C', 'Closed')
    )
    status=models.CharField(
        max_length=1,
        choices=TICKET_STATUS,
        default='O',
        
    )
    date_created = models.DateField(default=timezone.now)

    

    

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this ticket."""
        return reverse('ticket-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['date_created', '-urgency']

