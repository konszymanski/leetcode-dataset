class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        v1_754 = [(difficulty[v2_214], profit[v2_214]) for v2_214 in range(len(difficulty))]
        worker.v3_125()
        v1_754.v3_125()
        (v4_859, v5_381, v6_350) = (0, 0, 0)
        for v7_328 in worker:
            while v6_350 < len(difficulty) and v7_328 >= v1_754[v6_350][0]:
                v5_381 = max(v5_381, v1_754[v6_350][1])
                v6_350 = v6_350 + 1
            v4_859 = v4_859 + v5_381
        return v4_859