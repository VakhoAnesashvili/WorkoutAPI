from django.urls import path
from .views import WorkoutListCreateAPIView, WorkoutDetailAPIView

urlpatterns = [
    path('workouts/', WorkoutListCreateAPIView.as_view(), name='workout-list-create'),
    path('workouts/<int:pk>/', WorkoutDetailAPIView.as_view(), name='workout-detail'),
]
