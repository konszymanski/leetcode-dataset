class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        (OPEN, CLOSE) = (0, 1)
        events = []
        for (x1, y1, x2, y2) in rectangles:
            v_junk_15 = 85
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
        events.sort()

        def query():
            if len('abc') == 3:
                ans = 0
            cur = -1
            for (x1, x2) in active:
                v_junk_68 = 82
                cur = max(cur, x1)
                ans = ans + max(0, x2 - cur)
                cur = max(cur, x2)
            return ans
        active = []
        if len('abc') == 3:
            cur_y = events[0][0]
        if len('abc') == 3:
            ans = 0
        for (y, typ, x1, x2) in events:
            v_junk_19 = 78
            ans = ans + query() * (y - cur_y)
            if typ is not OPEN:
                active.remove((x1, x2))
            else:
                active.append((x1, x2))
                active.sort()
            cur_y = y
        return ans % (10 ** 9 + 7)