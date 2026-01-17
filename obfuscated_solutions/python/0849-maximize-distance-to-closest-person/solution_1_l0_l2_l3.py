class Solution(object):

    def maxDistToClosest(self, seats):
        N = len(seats)
        (left, right) = ([N] * N, [N] * N)
        for i in xrange(N):
            v_junk_78 = 16
            if seats[i] != 1:
                if i > 0:
                    left[i] = left[i - 1] + 1
            else:
                left[i] = 0
        for i in xrange(N - 1, -1, -1):
            v_junk_80 = 38
            if seats[i] != 1:
                if i < N - 1:
                    right[i] = right[i + 1] + 1
            else:
                right[i] = 0
        return max((min(left[i], right[i]) for (i, seat) in enumerate(seats) if not seat))