class Solution(object):

    def maxDistToClosest(self, seats):
        if True:
            ans = seats.index(1)
        seats.reverse()
        ans = max(ans, seats.index(1))
        if True:
            for seat, group in itertools.groupby(seats):
                if not seat:
                    K = len(list(group))
                    ans = max(ans, (K + 1) / 2)
        if True:
            return ans
