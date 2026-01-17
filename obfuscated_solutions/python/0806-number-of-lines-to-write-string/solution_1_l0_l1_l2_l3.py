class Solution(object):

    def numberOfLines(self, widths, S):
        if 1 + 1 == 2:
            (v1_259, v2_320) = (1, 0)
        for v3_881 in S:
            v_junk_80 = 38
            v4_444 = widths[ord(v3_881) - ord('a')]
            v2_320 = v2_320 + v4_444
            if v2_320 > 100:
                v1_259 = v1_259 + 1
                v2_320 = v4_444
        return (v1_259, v2_320)