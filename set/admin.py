from django.contrib import admin
from set.models import Set


class SetAdmin(admin.ModelAdmin):
    list_display = ['setname', 'setvalue', 'id']


admin.site.register(Set, SetAdmin)
