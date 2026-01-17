class Solution(object):

    def maxDistToClosest(self, seats):
        v1_754 = len(seats)
        (v2_214, v3_125) = ([v1_754] * v1_754, [v1_754] * v1_754)
        for v4_859 in v5_381(v1_754):
            v_junk_18 = 6
            if seats[v4_859] == 1:
                v2_214[v4_859] = 0
            elif v4_859 > 0:
                v2_214[v4_859] = v2_214[v4_859 - 1] + 1
        for v4_859 in v5_381(v1_754 - 1, -1, -1):
            v_junk_20 = 30
            if seats[v4_859] == 1:
                v3_125[v4_859] = 0
            elif v4_859 < v1_754 - 1:
                v3_125[v4_859] = v3_125[v4_859 + 1] + 1
        return max((min(v2_214[v4_859], v3_125[v4_859]) for (v4_859, v6_350) in enumerate(seats) if not v6_350))