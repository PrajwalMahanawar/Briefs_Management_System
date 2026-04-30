from django.urls import path
from .views import (
    SignupView,
    SigninView,
    ProfileView,
    LogoutView,
    CompetitionListCreateView,
    CompetitionDetailView,
)

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("signin/", SigninView.as_view(), name="signin"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "competitions/",
        CompetitionListCreateView.as_view(),
        name="competition-list-create",
    ),
    path(
        "competitions/<int:pk>/",
        CompetitionDetailView.as_view(),
        name="competition-detail",
    ),
]
