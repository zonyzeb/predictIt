from django.contrib import admin

# Register your models here.
from .models import Team, Prediction, Match

# Register your models here.
admin.site.register(Team)
admin.site.register(Match)