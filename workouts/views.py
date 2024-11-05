from rest_framework import generics
from .models import Workout
from .serializers import WorkoutSerializer

# list create (GET, POST) view 
class WorkoutListCreateView(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

# retrieve (GET) view
class WorkoutRetrieveView(generics.RetrieveAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

# update (PUT) view
class WorkoutUpdateView(generics.UpdateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

# destroy (DELETE) view
class WorkoutDestroyView(generics.DestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
