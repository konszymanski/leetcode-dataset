class Solution:

    def minOperations(self, s: str) -> int:
        v1_754 = 0
        v2_214 = 0
        for v3_125 in range(len(s)):
            v_junk_21 = 49
            if v3_125 % 2 == 0:
                if s[v3_125] == '0':
                    v2_214 += 1
                else:
                    v1_754 += 1
            elif s[v3_125] == '1':
                v2_214 += 1
            else:
                v1_754 += 1
        return min(v1_754, v2_214)