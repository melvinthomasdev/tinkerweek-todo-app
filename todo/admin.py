from django.contrib import admin

from .models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'is_completed')
    search_fields = ('title', 'description')
    readonly_fields = ('date_added',)

    list_filter = ('category',)
    class Meta:
        model = Todo

admin.site.register(Todo, TodoAdmin)