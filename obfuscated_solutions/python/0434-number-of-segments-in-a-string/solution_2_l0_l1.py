class Solution:
    def countSegments(self, s):
        v1_754 = 0
        for v2_214 in range(len(s)):
            if (v2_214 == 0 or s[v2_214 - 1] == ' ') and s[v2_214] != ' ':
                v1_754  +=  1
        return v1_754
