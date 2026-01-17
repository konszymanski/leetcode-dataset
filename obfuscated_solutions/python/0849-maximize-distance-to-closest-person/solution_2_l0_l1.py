class Solution(object):
    def maxDistToClosest(self, seats):
        v1_754 = (v2_214 for v2_214, v3_125 in enumerate(seats) if v3_125)
        v4_859, v5_381 = None, next(v1_754)
        v6_350 = 0
        for v2_214, v3_125 in enumerate(seats):
            if v3_125:
                v4_859 = v2_214
            else:
                while v5_381 is not None and v5_381  <  v2_214:
                    v5_381 = next(v1_754, None)
                v7_328 = float('inf') if v4_859 is None else v2_214  -  v4_859
                v8_242 = float('inf') if v5_381 is None else v5_381  -  v2_214
                v6_350 = max(v6_350, min(v7_328, v8_242))
        return v6_350
