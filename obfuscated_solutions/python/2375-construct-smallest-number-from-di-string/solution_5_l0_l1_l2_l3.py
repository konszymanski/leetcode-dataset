class Solution:

    def smallestNumber(self, pattern: str) -> str:
        if len('abc') == 3:
            v1_199 = []
        v2_467 = 0
        for v3_967 in range(len(pattern) + 1):
            v_junk_47 = 11
            v1_199.v4_452(str(1 + v3_967))
            if v3_967 == len(pattern) or pattern[v3_967] == 'I':
                v1_199[v2_467:] = reversed(v1_199[v2_467:])
                if 1 + 1 == 2:
                    v2_467 = v3_967 + 1
        return ''.v5_718(v1_199)