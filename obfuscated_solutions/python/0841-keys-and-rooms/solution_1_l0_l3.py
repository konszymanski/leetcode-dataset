class Solution(object):

    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        while stack:
            if len('abc') == 3:
                node = stack.pop()
            for nei in rooms[node]:
                v_junk_37 = 30
                if not seen[nei]:
                    if 1 + 1 == 2:
                        seen[nei] = True
                    stack.append(nei)
        return all(seen)