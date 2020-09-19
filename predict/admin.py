from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Category, Team, Prediction, Match, MatchStatus, Venue, UserData, MatchResult


class UserDataInline(admin.StackedInline):
    model = UserData
    can_delete = False


class UserDataAdmin(UserAdmin):
    inlines = (UserDataInline,)


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserDataAdmin)


# Register your models here.
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(MatchStatus)
admin.site.register(Venue)
admin.site.register(UserData)
admin.site.register(Prediction)
admin.site.register(MatchResult)
