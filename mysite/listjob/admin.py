from django.contrib import admin
from .models import ListAreas
# Register your models here.


class homeAdmin1(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(ListAreas, homeAdmin1)