from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user', 'completed_at']  # Users shouldn't modify these

    def validate_due_date(self, value):
        """Ensure due date is in the future."""
        from datetime import date
        if value < date.today():
            raise serializers.ValidationError("Due date must be in the future.")
        return value
