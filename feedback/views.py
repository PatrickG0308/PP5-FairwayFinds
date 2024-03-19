from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Feedback
from django.urls import reverse_lazy
from .forms import FeedbackForm

class Feedback(generic.ListView):
    """ This view is used to display all feedback """
    model = Feedback
    template_name = 'feedback/feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class AddFeedback(
        LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):

    """This view is used to allow a user to add a feedback"""
    form_class = FeedbackForm
    template_name = 'feedback/add_feedback.html'
    success_message = "Your feedback was added successfully"

    def form_valid(self, form):
        """
        Override the form_valid() method in model form view
        in order to set the signed in user as the name on the feedback.
        """
        form.instance.name = self.request.user
        return super().form_valid(form)


class EditFeedback(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.UpdateView):

    """
    This view is used to allow logged in users to edit their own feedback
    """
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/edit_feedback.html'
    success_message = "Feedback edited successfully"

    def test_func(self):
        """
        Prevent another user from editing user's feedback
        """
        feedback = self.get_object()
        return feedback.name == self.request.user or self.request.user.is_superuser


class DeleteFeedback(
        LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This view is used to allow logged in users to delete their own feedback
    """
    model = Feedback
    template_name = 'feedback/delete_feedback.html'
    success_message = "Feedback successfully deleted"
    success_url = reverse_lazy('feedback')

    def test_func(self):
        """
        Prevent another user from deleting another user's feedback
        """
        feedback= self.get_object()
        return feedback.name == self.request.user or self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display success message since SuccessMessageMixin
        cannot be used in generic.DeleteView.
        """
        messages.success(self.request, self.success_message)
        return super(DeleteFeedback, self).delete(request, *args, **kwargs)
