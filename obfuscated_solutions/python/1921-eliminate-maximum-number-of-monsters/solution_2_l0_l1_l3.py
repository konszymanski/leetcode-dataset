import heapq

class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        v1_754 = []
        for v2_214 in range(len(dist)):
            v_junk_10 = 98
            v1_754.v3_125(dist[v2_214] / speed[v2_214])
        v4_859.v5_381(v1_754)
        v6_350 = 0
        while v1_754:
            if v4_859.v7_328(v1_754) <= v6_350:
                break
            v6_350 += 1
        return v6_350