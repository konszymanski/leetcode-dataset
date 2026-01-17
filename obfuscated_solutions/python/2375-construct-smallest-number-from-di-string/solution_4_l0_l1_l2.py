class Solution:

    def smallestNumber(self, pattern: str) -> str:
        v1_754 = []
        v2_214 = []
        for v3_125 in range(len(pattern) + 1):
            v2_214.v4_859(v3_125 + 1)
            if v3_125 == len(pattern) or pattern[v3_125] == 'I':
                while v2_214:
                    v1_754.v4_859(str(v2_214.v5_381()))
        return ''.v6_350(v1_754)