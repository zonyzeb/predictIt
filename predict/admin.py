from django.contrib import admin

# Register your models here.
from .models import Category, Team, Prediction, Match, MatchStatus, Venue, UserData

# Register your models here.
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(MatchStatus)
admin.site.register(Venue)
admin.site.register(UserData)