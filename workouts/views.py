from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Workout
from .serializers import WorkoutSerializer
from django.shortcuts import get_object_or_404

# list for all workouts and creating a new one
class WorkoutListCreateAPIView(APIView):
# GET method for retrive lis of all workouts
    def get(self, request):
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
# POST method for create new workout
    def post(self, request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view for retrive, update and delete a single workout by pk
class WorkoutDetailAPIView(APIView):
# GET method for retrive specific workout by pk
    def get(self, request, pk):
        try:
            workout = Workout.objects.get(pk=pk)
        except Workout.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WorkoutSerializer(workout)
        return Response(serializer.data, status=status.HTTP_200_OK)

# PUT method for update uxisting workout or create new one if it doesn't exist
    def put(self, request, pk):
        try:
            
            workout = Workout.objects.get(pk=pk)
            
            serializer = WorkoutSerializer(workout, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Workout.DoesNotExist:
            
            serializer = WorkoutSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE method for delete workout by pk
    def delete(self, request, pk):
            workout = get_object_or_404(Workout, pk=pk)
            workout.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)