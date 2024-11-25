from django.contrib import admin
from .models import GuestBook, MyProject

@admin.register(MyProject)
class MyProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

@admin.register(GuestBook)
class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'message')
