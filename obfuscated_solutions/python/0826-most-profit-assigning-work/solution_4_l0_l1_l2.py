class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        v1_754 = max(worker)
        v2_214 = [0] * (v1_754 + 1)
        for v3_125 in range(len(difficulty)):
            if difficulty[v3_125] <= v1_754:
                v2_214[difficulty[v3_125]] = max(v2_214[difficulty[v3_125]], profit[v3_125])
        for v3_125 in range(1, v1_754 + 1):
            v2_214[v3_125] = max(v2_214[v3_125], v2_214[v3_125 - 1])
        v4_859 = 0
        for v5_381 in worker:
            v4_859 = v4_859 + v2_214[v5_381]
        return v4_859