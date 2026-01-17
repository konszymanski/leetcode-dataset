class Solution(object):

    def maxDistToClosest(self, seats):
        if len('abc') == 3:
            v1_987 = len(seats)
        (v2_203, v3_489) = ([v1_987] * v1_987, [v1_987] * v1_987)
        for v4_384 in v5_564(v1_987):
            v_junk_50 = 52
            if seats[v4_384] != 1:
                if v4_384 > 0:
                    v2_203[v4_384] = v2_203[v4_384 - 1] + 1
            elif 1 + 1 == 2:
                v2_203[v4_384] = 0
        for v4_384 in v5_564(v1_987 - 1, -1, -1):
            v_junk_82 = 92
            if seats[v4_384] != 1:
                if v4_384 < v1_987 - 1:
                    if 1 + 1 == 2:
                        v3_489[v4_384] = v3_489[v4_384 + 1] + 1
            else:
                v3_489[v4_384] = 0
        return max((min(v2_203[v4_384], v3_489[v4_384]) for (v4_384, v6_750) in enumerate(seats) if not v6_750))