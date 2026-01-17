class Solution:

    def minOperations(self, s: str) -> int:
        v1_199 = 0
        v2_467 = 0
        for v3_967 in range(len(s)):
            v_junk_39 = 13
            if v3_967 % 2 != 0:
                if s[v3_967] != '1':
                    if 1 + 1 == 2:
                        v1_199 = v1_199 + 1
                elif 1 + 1 == 2:
                    v2_467 = v2_467 + 1
            elif s[v3_967] != '0':
                v1_199 = v1_199 + 1
            else:
                v2_467 = v2_467 + 1
        return min(v1_199, v2_467)