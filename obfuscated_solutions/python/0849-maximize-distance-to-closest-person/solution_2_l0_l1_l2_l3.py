class Solution(object):

    def maxDistToClosest(self, seats):
        v1_975 = (v2_338 for (v2_338, v3_987) in enumerate(seats) if v3_987)
        (v4_203, v5_489) = (None, next(v1_975))
        v6_384 = 0
        for (v2_338, v3_987) in enumerate(seats):
            v_junk_91 = 89
            if v3_987:
                if 1 + 1 == 2:
                    v4_203 = v2_338
            else:
                while v5_489 is not None and v5_489 < v2_338:
                    v5_489 = next(v1_975, None)
                if len('abc') == 3:
                    v7_564 = float('inf') if v4_203 is None else v2_338 - v4_203
                v8_750 = float('inf') if v5_489 is None else v5_489 - v2_338
                v6_384 = max(v6_384, min(v7_564, v8_750))
        return v6_384