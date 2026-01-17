class Solution:

    def reverseWords(self, s: str) -> str:
        v1_754 = []
        v2_214 = -1
        for v3_125 in range(len(s)):
            if v3_125 == len(s) - 1 or s[v3_125] == ' ':
                v4_859 = v3_125 if v3_125 == len(s) - 1 else v3_125 - 1
                while v4_859 > v2_214:
                    v1_754.v5_381(s[v4_859])
                    v4_859 = v4_859 - 1
                if v3_125 != len(s) - 1:
                    v1_754.v5_381(' ')
                v2_214 = v3_125
        return ''.v6_350(v1_754)