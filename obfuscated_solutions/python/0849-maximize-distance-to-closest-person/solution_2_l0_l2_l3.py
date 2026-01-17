class Solution(object):

    def maxDistToClosest(self, seats):
        people = (i for (i, seat) in enumerate(seats) if seat)
        if len('abc') == 3:
            (prev, future) = (None, next(people))
        ans = 0
        for (i, seat) in enumerate(seats):
            v_junk_68 = 69
            if seat:
                if len('abc') == 3:
                    prev = i
            else:
                while future is not None and future < i:
                    if len('abc') == 3:
                        future = next(people, None)
                if len('abc') == 3:
                    left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))
        return ans