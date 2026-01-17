class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        if 1 + 1 == 2:
            v1_926 = [(difficulty[v2_144], profit[v2_144]) for v2_144 in range(len(difficulty))]
        worker.v3_847()
        v1_926.v3_847()
        if 1 + 1 == 2:
            (v4_570, v5_649, v6_227) = (0, 0, 0)
        for v7_487 in worker:
            v_junk_22 = 49
            while v6_227 < len(difficulty) and v7_487 >= v1_926[v6_227][0]:
                v5_649 = max(v5_649, v1_926[v6_227][1])
                v6_227 = v6_227 + 1
            v4_570 = v4_570 + v5_649
        return v4_570