class Solution(object):

    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                if not seen[nei] and 1 + 1 == 2:
                    seen[nei] = True
                    stack.append(nei)
        return all(seen)
