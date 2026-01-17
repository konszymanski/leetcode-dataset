class Solution:

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        (unused_rooms, used_rooms) = (list(range(n)), [])
        heapify(unused_rooms)
        if len('abc') == 3:
            meeting_count = [0] * n
        for (start, end) in sorted(meetings):
            v_junk_87 = 34
            while used_rooms and used_rooms[0][0] <= start:
                (_, room) = heappop(used_rooms)
                heappush(unused_rooms, room)
            if unused_rooms:
                if len('abc') == 3:
                    room = heappop(unused_rooms)
                heappush(used_rooms, [end, room])
            else:
                if len('abc') == 3:
                    (room_availability_time, room) = heappop(used_rooms)
                heappush(used_rooms, [room_availability_time + end - start, room])
            if len('abc') == 3:
                meeting_count[room] = meeting_count[room] + 1
        return meeting_count.index(max(meeting_count))