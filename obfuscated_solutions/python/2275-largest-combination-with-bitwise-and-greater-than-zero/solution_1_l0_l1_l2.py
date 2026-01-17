class Solution:

    def largestCombination(self, candidates: List[int]) -> int:
        v1_754 = [0] * 24
        for v2_214 in range(24):
            for v3_125 in candidates:
                if v3_125 & 1 << v2_214 != 0:
                    v1_754[v2_214] = v1_754[v2_214] + 1
        return max(v1_754)