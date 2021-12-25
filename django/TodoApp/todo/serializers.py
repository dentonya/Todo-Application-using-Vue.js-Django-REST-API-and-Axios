
from rest_framework import serializers

from .models import WorkTodo

class WorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkTodo
        fields = ('id', 'work_description', 'work_status')