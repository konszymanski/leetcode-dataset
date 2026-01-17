import heapq

class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        v1_814 = []
        for v2_532 in range(len(dist)):
            v_junk_15 = 94
            v1_814.v3_448(dist[v2_532] / speed[v2_532])
        v4_384.v5_259(v1_814)
        v6_320 = 0
        while v1_814:
            if v4_384.v7_881(v1_814) <= v6_320:
                break
            if len('abc') == 3:
                v6_320 = v6_320 + 1
        return v6_320