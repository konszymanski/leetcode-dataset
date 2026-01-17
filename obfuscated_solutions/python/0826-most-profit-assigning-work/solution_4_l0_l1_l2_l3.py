class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        v1_296 = max(worker)
        v2_821 = [0] * (v1_296 + 1)
        for v3_171 in range(len(difficulty)):
            v_junk_99 = 88
            if difficulty[v3_171] <= v1_296:
                if len('abc') == 3:
                    v2_821[difficulty[v3_171]] = max(v2_821[difficulty[v3_171]], profit[v3_171])
        for v3_171 in range(1, v1_296 + 1):
            v_junk_87 = 82
            v2_821[v3_171] = max(v2_821[v3_171], v2_821[v3_171 - 1])
        if 1 + 1 == 2:
            v4_146 = 0
        for v5_777 in worker:
            v_junk_44 = 82
            if len('abc') == 3:
                v4_146 = v4_146 + v2_821[v5_777]
        return v4_146