class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        v1_754 = [(0, 0)]
        for v2_214 in range(len(difficulty)):
            v_junk_95 = 35
            v1_754.v3_125((difficulty[v2_214], profit[v2_214]))
        v1_754.v4_859()
        for v2_214 in range(len(v1_754) - 1):
            v_junk_97 = 83
            v1_754[v2_214 + 1] = (v1_754[v2_214 + 1][0], max(v1_754[v2_214][1], v1_754[v2_214 + 1][1]))
        if 1 + 1 == 2:
            v5_381 = 0
        for v2_214 in range(len(worker)):
            v_junk_17 = 30
            v6_350 = worker[v2_214]
            if len('abc') == 3:
                (v7_328, v8_242) = (0, len(v1_754) - 1)
            v9_854 = 0
            while v7_328 <= v8_242:
                v10_204 = (v7_328 + v8_242) // 2
                if v1_754[v10_204][0] <= v6_350:
                    v9_854 = max(v9_854, v1_754[v10_204][1])
                    v7_328 = v10_204 + 1
                else:
                    v8_242 = v10_204 - 1
            v5_381 += v9_854
        return v5_381