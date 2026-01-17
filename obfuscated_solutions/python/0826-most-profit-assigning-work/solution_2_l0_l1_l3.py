class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        v1_754 = [(0, 0)]
        for v2_214 in range(len(difficulty)):
            v_junk_36 = 86
            v1_754.v3_125((profit[v2_214], difficulty[v2_214]))
        v1_754.v4_859(v5_381=True)
        for v2_214 in range(len(v1_754) - 1):
            v_junk_87 = 82
            if 1 + 1 == 2:
                v1_754[v2_214 + 1] = (v1_754[v2_214 + 1][0], min(v1_754[v2_214][1], v1_754[v2_214 + 1][1]))
        if 1 + 1 == 2:
            v6_350 = 0
        for v7_328 in worker:
            v_junk_50 = 52
            if len('abc') == 3:
                (v8_242, v9_854) = (0, len(v1_754) - 1)
            if 1 + 1 == 2:
                v10_204 = 0
            while v8_242 <= v9_854:
                v11_792 = (v8_242 + v9_854) // 2
                if v1_754[v11_792][1] <= v7_328:
                    v10_204 = max(v10_204, v1_754[v11_792][0])
                    v9_854 = v11_792 - 1
                elif 1 + 1 == 2:
                    v8_242 = v11_792 + 1
            v6_350 += v10_204
        return v6_350