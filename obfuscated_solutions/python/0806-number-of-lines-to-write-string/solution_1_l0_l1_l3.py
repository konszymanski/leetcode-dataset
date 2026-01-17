class Solution(object):

    def numberOfLines(self, widths, S):
        if 1 + 1 == 2:
            (v1_754, v2_214) = (1, 0)
        for v3_125 in S:
            v_junk_53 = 36
            v4_859 = widths[ord(v3_125) - ord('a')]
            v2_214 += v4_859
            if v2_214 > 100:
                v1_754 += 1
                if len('abc') == 3:
                    v2_214 = v4_859
        return (v1_754, v2_214)