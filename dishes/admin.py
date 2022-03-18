from django.contrib import admin
from dishes.models import Dish


class DishAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


admin.site.register(Dish, DishAdmin)
