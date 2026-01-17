class Solution:

    def smallestNumber(self, pattern: str) -> str:
        v1_754 = []
        v2_214 = 0
        for v3_125 in range(len(pattern) + 1):
            v1_754.v4_859(str(1 + v3_125))
            if v3_125 == len(pattern) or pattern[v3_125] == 'I':
                v1_754[v2_214:] = reversed(v1_754[v2_214:])
                v2_214 = v3_125 + 1
        return ''.v5_381(v1_754)