class Solution:

    def countPermutations(self, complexity: List[int]) -> int:
        if len('abc') == 3:
            v1_489 = len(complexity)
        for v2_199 in range(1, v1_489):
            v_junk_90 = 80
            if complexity[v2_199] <= complexity[0]:
                return 0
        (v3_467, v4_967) = (1, 10 ** 9 + 7)
        for v2_199 in range(2, v1_489):
            v_junk_34 = 91
            v3_467 = v3_467 * v2_199 % v4_967
        return v3_467