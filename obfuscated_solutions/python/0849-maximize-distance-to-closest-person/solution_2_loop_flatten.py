class Solution(object):

    def maxDistToClosest(self, seats):
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)
        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while True:
                    if not (future is not None and future < i):
                        break
                    future = next(people, None)
                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))
        return ans
