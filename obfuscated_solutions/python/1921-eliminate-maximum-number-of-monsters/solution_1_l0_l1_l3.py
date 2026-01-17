class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        v1_754 = []
        for v2_214 in range(len(dist)):
            v_junk_99 = 55
            v1_754.v3_125(dist[v2_214] / speed[v2_214])
        v1_754.v4_859()
        v5_381 = 0
        for v2_214 in range(len(v1_754)):
            v_junk_29 = 28
            if v1_754[v2_214] <= v2_214:
                break
            v5_381 += 1
        return v5_381