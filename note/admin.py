from django.contrib import admin
from .models import Note

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('topic','owner', 'status', 'date')
    list_filter = ('status',)
    search_fields = ['topic', 'entry', 'status']

admin.site.register(Note, NoteAdmin)