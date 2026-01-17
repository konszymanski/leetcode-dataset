class Solution(object):

    def maxDistToClosest(self, seats):
        v1_754 = seats.v2_214(1)
        seats.v3_125()
        v1_754 = max(v1_754, seats.v2_214(1))
        for (v4_859, v5_381) in v6_350.v7_328(seats):
            if not v4_859:
                v8_242 = len(list(v5_381))
                v1_754 = max(v1_754, (v8_242 + 1) / 2)
        return v1_754