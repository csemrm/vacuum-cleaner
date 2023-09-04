"""
Views for the Vacuum Cleaner APIs.
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VacuumCleanerSerializer


class VacuumCleanerDataView(APIView):
    """
        Vacuum Cleaner Data View will receive cleaning_batches, priority_rooms
        data from the api/vacuum endpoint via the post method.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to clean rooms using a vacuum cleaner.

        Args:
            request (HttpRequest): The HTTP request object.
            In request object cleaning_batches, priority_rooms data
            will available for process implementation.

        Returns:
            Response: An HTTP response with cleaning results with 5
            outputs Like:
            traversal_path: The actual path the vacuum took as arrays of
            rooms (An array of arrays showcasing its actual traversal of rooms)
            total_cleaned: # of rooms it cleaned in total
            total_batches: # of batches it processed
            total_unvisited: # of rooms it passed without cleaning either
            going left or right
            final_room: The final (current) room the vacuum cleaner is in
        """
        serializer = VacuumCleanerSerializer(data=request.data)

        if serializer.is_valid():
            cleaning_data = serializer.validated_data
            result = self.vacuum_cleaner(cleaning_data['cleaning_batches'], cleaning_data['priority_rooms'])
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def vacuum_cleaner(self, cleaning_batches, priority_rooms):
        """
                Simulate a vacuum cleaner cleaning algorithm.

                Args:
            request (HttpRequest): The HTTP request object.
            In request object cleaning_batches, priority_rooms data
            will available for process implementation.

        Returns:
            An response with cleaning results with 5
            outputs like:
            traversal_path: The actual path the vacuum took as arrays of
            rooms (An array of arrays showcasing its actual traversal of rooms)
            total_cleaned: # of rooms it cleaned in total
            total_batches: # of batches it processed
            total_unvisited: # of rooms it passed without cleaning either
            going left or right
            final_room: The final (current) room the vacuum cleaner is in
        """
        current_room = 1
        cleaned_rooms = set()
        traversed_rooms = []
        total_cleaned = 0
        total_batches = 0
        total_unvisited = 0

        for batch in cleaning_batches:
            total_batches += 1
            print('batch', batch)
            priority_rooms_in_batch = set(priority_rooms) & set(batch)
            print('priority_room', priority_rooms_in_batch)
            # Visit priority rooms first
            for room in priority_rooms_in_batch:
                print('priority_room: ', room, current_room)
                # room = 7 < current_room =1
                # checking cleaner moving directions for priority rooms
                if room < current_room:
                    rooms = range(current_room - 1, room, -1)
                    total_unvisited += len(rooms)
                    traversed_rooms.extend(rooms)
                else:
                    rooms = range(current_room + 1, room)
                    total_unvisited += len(rooms)
                    traversed_rooms.extend(rooms)
                current_room = room
                cleaned_rooms.add(current_room)
                total_cleaned += 1
                traversed_rooms.append(current_room)

            # Visit Non-priority rooms in the batch
            print('Visit rooms in the batch: ', batch)
            for room in batch:
                print('Visit other room in the batch: ', room)
                if room != current_room and room not in priority_rooms:
                    print('Visit room and current_room in the batch: ', room, current_room)

                    # checking cleaner moving directions for non-priority rooms

                    if room < current_room:
                        rooms = range(current_room - 1, room, -1)
                        total_unvisited += len(rooms)
                        traversed_rooms.extend(rooms)
                    else:
                        rooms = range(current_room + 1, room)
                        total_unvisited += len(rooms)
                        traversed_rooms.extend(rooms)

                    current_room = room
                    cleaned_rooms.add(current_room)
                    total_cleaned += 1
                    traversed_rooms.append(current_room)

                elif room == current_room and room not in priority_rooms:
                    cleaned_rooms.add(room)
                    total_cleaned += 1

        return {
            "traversal_path": traversed_rooms,
            "total_cleaned": total_cleaned,
            "total_batches": total_batches,
            "total_unvisited": total_unvisited,
            "final_room": current_room,
        }
