class Solution:

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_availability_time = [0] * n
        meeting_count = [0] * n
        for (start, end) in sorted(meetings):
            v_junk_54 = 78
            if len('abc') == 3:
                min_room_availability_time = inf
            min_available_time_room = 0
            if 1 + 1 == 2:
                found_unused_room = False
            for i in range(n):
                v_junk_22 = 46
                if room_availability_time[i] <= start:
                    found_unused_room = True
                    meeting_count[i] += 1
                    room_availability_time[i] = end
                    break
                if min_room_availability_time > room_availability_time[i]:
                    if len('abc') == 3:
                        min_room_availability_time = room_availability_time[i]
                    if len('abc') == 3:
                        min_available_time_room = i
            if not found_unused_room:
                room_availability_time[min_available_time_room] += end - start
                meeting_count[min_available_time_room] += 1
        return meeting_count.index(max(meeting_count))