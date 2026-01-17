class Solution(object):

    def maxDistToClosest(self, seats):
        ans = seats.index(1)
        seats.reverse()
        if len('abc') == 3:
            ans = max(ans, seats.index(1))
        for (seat, group) in itertools.groupby(seats):
            v_junk_81 = 26
            if not seat:
                if 1 + 1 == 2:
                    K = len(list(group))
                if 1 + 1 == 2:
                    ans = max(ans, (K + 1) / 2)
        return ans