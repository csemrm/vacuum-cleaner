from rest_framework import serializers

class VacuumCleanerSerializer(serializers.Serializer):
    cleaning_batches = serializers.ListField(child=serializers.ListField())
    priority_rooms = serializers.ListField()
