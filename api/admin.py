from django.contrib import admin
from .models import Hackathon, HackathonParticipant, Submission

# Register your models here.
admin.site.register(Hackathon)
admin.site.register(HackathonParticipant)
admin.site.register(Submission)