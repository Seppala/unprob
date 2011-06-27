from splash.models import Entry
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entry)

class EntryAdmin(admin.ModelAdmin):
	list_display = ('email', 'problem')