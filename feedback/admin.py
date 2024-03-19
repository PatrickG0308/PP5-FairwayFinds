from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    """Allows admin to manage Feedback via the admin panel"""
    list_display = (
        'name',
        'created_on'
    )

admin.site.register(Feedback, FeedbackAdmin)   
