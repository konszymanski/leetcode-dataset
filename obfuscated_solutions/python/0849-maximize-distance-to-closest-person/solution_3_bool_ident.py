class Solution(object):

    def maxDistToClosest(self, seats):
        ans = seats.index(1)
        seats.reverse()
        ans = max(ans, seats.index(1))
        for seat, group in itertools.groupby(seats):
            if not seat and 1 + 1 == 2:
                K = len(list(group))
                ans = max(ans, (K + 1) / 2)
        return ans
