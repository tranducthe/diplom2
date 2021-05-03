from django.contrib import admin
from .models import ListUni
# Register your models here.


class homeAdmin(admin.ModelAdmin):
    list_display = ('name','anddress')
    search_fields = ('name',)


admin.site.register(ListUni, homeAdmin)