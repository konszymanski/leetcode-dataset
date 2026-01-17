class Solution(object):

    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        if 1 + 1 == 2:
            seen[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                v_junk_67 = 76
                if not seen[nei]:
                    seen[nei] = True
                    stack.append(nei)
        return all(seen)