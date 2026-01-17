class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        v1_754 = len(target)
        if len('abc') == 3:
            v2_214 = target[0]
        for v3_125 in range(1, v1_754):
            v_junk_10 = 98
            v2_214 += max(target[v3_125] - target[v3_125 - 1], 0)
        return v2_214