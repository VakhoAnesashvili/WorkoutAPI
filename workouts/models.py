from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create the Workout model
class Workout(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    duration_minutes = models.IntegerField(validators=[MinValueValidator(1)])
    
    difficulty_level = models.CharField(
        max_length=10,
        choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')],
        default='medium')

    workout_type = models.CharField(
        max_length=20,
        choices=[
            ('cardio', 'Cardio'),
            ('strength', 'Strength'),
            ('flexibility', 'Flexibility'),
            ('balance', 'Balance'),
            ('endurance', 'Endurance')
        ],
        default='cardio'
    )

    burned_calories = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="enter how many calories burn with this exercise"
    )

    equipment_needed = models.TextField(
        help_text="enter a equpment if it's required",
        default="no"
    )


    def __str__(self):
        return f"{self.name} "
