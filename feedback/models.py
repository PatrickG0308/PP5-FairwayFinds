from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Feedback (models.Model):
    """Model for Feedback"""
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedback")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """ To display the feedback by created_on in ascending order """
        ordering = ['created_on']

    def get_absolute_url(self):
        """Get url after user adds/edits feedback"""
        return reverse('feedback')

    def __str__(self):
        return f"Feedback: {self.body} by {self.name}"
