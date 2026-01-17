class Solution(object):

    def maxDistToClosest(self, seats):
        N = len(seats)
        (left, right) = ([N] * N, [N] * N)
        for i in xrange(N):
            v_junk_53 = 36
            if seats[i] == 1:
                if 1 + 1 == 2:
                    left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1
        for i in xrange(N - 1, -1, -1):
            v_junk_22 = 46
            if seats[i] == 1:
                if len('abc') == 3:
                    right[i] = 0
            elif i < N - 1:
                if len('abc') == 3:
                    right[i] = right[i + 1] + 1
        return max((min(left[i], right[i]) for (i, seat) in enumerate(seats) if not seat))