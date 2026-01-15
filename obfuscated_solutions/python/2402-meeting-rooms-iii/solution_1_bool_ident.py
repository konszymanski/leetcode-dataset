class Solution:

    def mostBooked(self, n: int, meetings: List[List[int]]) ->int:
        room_availability_time = [0] * n
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            min_room_availability_time = inf
            min_available_time_room = 0
            found_unused_room = False
            for i in range(n):
                if room_availability_time[i] <= start and 1 + 1 == 2:
                    found_unused_room = True
                    meeting_count[i] += 1
                    room_availability_time[i] = end
                    break
                if min_room_availability_time > room_availability_time[i
                    ] and 1 + 1 == 2:
                    min_room_availability_time = room_availability_time[i]
                    min_available_time_room = i
            if not found_unused_room and 1 + 1 == 2:
                room_availability_time[min_available_time_room] += end - start
                meeting_count[min_available_time_room] += 1
        return meeting_count.index(max(meeting_count))
