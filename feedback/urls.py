from django.urls import path
from . import views

urlpatterns = [
    path("", views.FeedbackList.as_view(), name="feedback"),
    path("feedback/add/", views.AddFeedback.as_view(), name="add_feedback"),
    path("feedback/edit/<int:pk>/", views.EditFeedback.as_view(), name="edit_feedback"),
    path(
        "feedback/delete/<int:pk>/",
        views.DeleteFeedback.as_view(),
        name="delete_feedback",
    ),
]
