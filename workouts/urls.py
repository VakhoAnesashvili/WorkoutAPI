from django.urls import path
from .views import WorkoutListCreateView, WorkoutRetrieveView, WorkoutUpdateView, WorkoutDestroyView

urlpatterns = [
    path('workouts/', WorkoutListCreateView.as_view(), name='workout-list-create'),
    path('workouts/<int:pk>/', WorkoutRetrieveView.as_view(), name='workout-detail'),
    path('workouts/<int:pk>/update/', WorkoutUpdateView.as_view(), name='workout-update'),
    path('workouts/<int:pk>/delete/', WorkoutDestroyView.as_view(), name='workout-delete')
]
