from django.contrib import admin
from tickets.models import Ticket, Department
# Register your models here.

admin.site.register(Ticket)
admin.site.register(Department)