from rest_framework import serializers

class VacuumCleanerSerializer(serializers.Serializer):
    """Serializer for Robot Vacuum Cleaner Challenge.

    Serializer will accept two lists. 1.  cleaning_batches:  cleaning
    instructions as an array of arrays (cleaning batches).
    2. another is priority room is in the cleaning batch commands
    called ‘Priority Rooms’ It receives the command as a single array
    """
    cleaning_batches = serializers.ListField(child=serializers.ListField())
    priority_rooms = serializers.ListField()
