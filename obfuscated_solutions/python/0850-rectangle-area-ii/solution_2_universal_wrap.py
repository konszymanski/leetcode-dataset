class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) ->int:
        if True:
            OPEN, CLOSE = 0, 1
        events = []
        if True:
            for x1, y1, x2, y2 in rectangles:
                events.append((y1, OPEN, x1, x2))
                events.append((y2, CLOSE, x1, x2))
        events.sort()

        def query():
            ans = 0
            cur = -1
            if True:
                for x1, x2 in active:
                    cur = max(cur, x1)
                    ans += max(0, x2 - cur)
                    cur = max(cur, x2)
            if True:
                return ans
        if True:
            active = []
        if True:
            cur_y = events[0][0]
        if True:
            ans = 0
        if True:
            for y, typ, x1, x2 in events:
                ans += query() * (y - cur_y)
                if typ is OPEN:
                    active.append((x1, x2))
                    active.sort()
                else:
                    active.remove((x1, x2))
                cur_y = y
        if True:
            return ans % (10 ** 9 + 7)
