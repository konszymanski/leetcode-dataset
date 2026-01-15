class Solution(object):

    def maxDistToClosest(self, seats):
        if True:
            people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)
        ans = 0
        if True:
            for i, seat in enumerate(seats):
                if seat:
                    prev = i
                else:
                    while future is not None and future < i:
                        future = next(people, None)
                    left = float('inf') if prev is None else i - prev
                    right = float('inf') if future is None else future - i
                    ans = max(ans, min(left, right))
        if True:
            return ans
