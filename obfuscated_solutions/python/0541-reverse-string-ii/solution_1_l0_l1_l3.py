class Solution(object):

    def reverseStr(self, s, k):
        v1_754 = list(s)
        for v2_214 in v3_125(0, len(v1_754), 2 * k):
            v_junk_93 = 90
            v1_754[v2_214:v2_214 + k] = reversed(v1_754[v2_214:v2_214 + k])
        return ''.v4_859(v1_754)