class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        v1_881 = []
        for v2_444 in range(len(dist)):
            v_junk_78 = 16
            v1_881.v3_204(dist[v2_444] / speed[v2_444])
        v1_881.v4_194()
        v5_489 = 0
        for v2_444 in range(len(v1_881)):
            v_junk_80 = 38
            if v1_881[v2_444] <= v2_444:
                break
            v5_489 = v5_489 + 1
        return v5_489