from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VacuumCleanerSerializer

class VacuumCleanerDataView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = VacuumCleanerSerializer(data=request.data)

        if serializer.is_valid():
            cleaning_data = serializer.validated_data
            result = self.vacuum_cleaner(cleaning_data['cleaning_batches'], cleaning_data['priority_rooms'])
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def vacuum_cleaner(self, cleaning_batches, priority_rooms):
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
                print('priority_room: ',room, current_room)
                # room = 7 < current_room =1
                if room < current_room:
                    rooms = range(current_room - 1, room - 1, -1)
                    print('priority total_unvisited: ', total_unvisited)
                    total_unvisited += len(rooms) - 1
                    print('priority total_unvisited: ', total_unvisited)
                    traversed_rooms.extend(rooms)
                else:
                    rooms = range(current_room + 1, room)
                    total_unvisited += len(rooms)
                    print('priority total_unvisited: ', total_unvisited)
                    print('priority total_unvisited rooms: ', list(rooms))
                    traversed_rooms.extend(rooms)
                current_room = room
                print('current_room: ', current_room)
                cleaned_rooms.add(current_room)
                print('cleaned_rooms: ', cleaned_rooms)
                total_cleaned += 1
                print('total_cleaned: ', total_cleaned)
                traversed_rooms.append(current_room)
                print('traversed_rooms: ', traversed_rooms)

            # Visit Non priority rooms in the batch
            print('Visit rooms in the batch: ', batch)
            for room in batch:
                print('Visit other room in the batch: ', room)
                if room != current_room and room not in priority_rooms:
                    print('Visit  room and current_room in the batch: ', room, current_room)
                    if room < current_room:
                        rooms = range(current_room - 1, room, -1)
                        total_unvisited += len(rooms)
                        traversed_rooms.extend(rooms)
                    else:
                        rooms = range(current_room + 1, room)
                        print('Visit rooms: ', list(rooms))
                        total_unvisited += len(rooms)
                        traversed_rooms.extend(rooms)

                    current_room = room
                    cleaned_rooms.add(current_room)
                    print('cleaned_rooms: ', cleaned_rooms)
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


