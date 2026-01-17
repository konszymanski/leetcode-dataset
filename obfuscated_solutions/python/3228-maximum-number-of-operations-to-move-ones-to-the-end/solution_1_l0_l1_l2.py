class Solution:

    def maxOperations(self, s: str) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 0
        while v3_125 < len(s):
            if s[v3_125] != '0':
                v1_754 = v1_754 + 1
            else:
                while v3_125 + 1 < len(s) and s[v3_125 + 1] == '0':
                    v3_125 = v3_125 + 1
                v2_214 = v2_214 + v1_754
            v3_125 = v3_125 + 1
        return v2_214