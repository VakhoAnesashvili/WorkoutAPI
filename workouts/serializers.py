from rest_framework import serializers
from .models import Workout


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = [
            'id',
            'name',
            'description',
            'duration_minutes',
            'difficulty_level',
            'workout_type',
            'burned_calories',
            'equipment_needed',
        ]
        

    def validate_name(self, name):
            request = self.context.get('request')
            if request and request.method == 'POST':
                if Workout.objects.filter(name=name).exists():
                    raise serializers.ValidationError("There is already an existing workout with the same name.")
            
            return name