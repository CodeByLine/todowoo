from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('title', 'need_by_date', 'quantity', 'created', 'user', 'important')

admin.site.register(Todo, TodoAdmin)

