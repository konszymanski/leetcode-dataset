class Solution:

    def countPermutations(self, complexity: List[int]) -> int:
        v1_754 = len(complexity)
        for v2_214 in range(1, v1_754):
            if complexity[v2_214] <= complexity[0]:
                return 0
        (v3_125, v4_859) = (1, 10 ** 9 + 7)
        for v2_214 in range(2, v1_754):
            v3_125 = v3_125 * v2_214 % v4_859
        return v3_125