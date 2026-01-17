class Solution(object):

    def maxDistToClosest(self, seats):
        if len('abc') == 3:
            people = (i for (i, seat) in enumerate(seats) if seat)
        if 1 + 1 == 2:
            (prev, future) = (None, next(people))
        if 1 + 1 == 2:
            ans = 0
        for (i, seat) in enumerate(seats):
            v_junk_45 = 1
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)
                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))
        return ans