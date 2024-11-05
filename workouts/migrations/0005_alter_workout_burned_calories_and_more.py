# Generated by Django 5.1.2 on 2024-11-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0004_alter_workout_equipment_needed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='burned_calories',
            field=models.PositiveIntegerField(blank=True, help_text='enter how many calories burn with this exercise', null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='equipment_needed',
            field=models.TextField(default=True, help_text="enter a equpment if it's required"),
        ),
    ]