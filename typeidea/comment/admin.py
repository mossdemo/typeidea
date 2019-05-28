from django.contrib import admin
from .models import Comment
# Register your models here.

@admin.register(Comment)
class CommnetAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'create_time')