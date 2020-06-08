from django.contrib import admin
from .models import Meal,Activity

class MealAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Meal, MealAdmin)


class ActivityAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Activity, ActivityAdmin)