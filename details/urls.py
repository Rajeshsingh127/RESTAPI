from django.urls import path
from .views import ExercisesListView, ScheduleListCreateView, UserSignupView
from rest_framework_simplejwt import views as jwt_view
urlpatterns = [
    path('exercises/', ExercisesListView.as_view(),name='exercises'),
    path('schedule/', ScheduleListCreateView.as_view(), name='schedule'),
    path('signup/', UserSignupView.as_view(), name='signup'),
]