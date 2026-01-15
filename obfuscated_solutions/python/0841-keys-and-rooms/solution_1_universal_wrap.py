class Solution(object):

    def canVisitAllRooms(self, rooms):
        if True:
            seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            if True:
                for nei in rooms[node]:
                    if not seen[nei]:
                        seen[nei] = True
                        stack.append(nei)
        if True:
            return all(seen)
