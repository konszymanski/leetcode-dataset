class Solution(object):

    def numberOfLines(self, widths, S):
        (lines, width) = (1, 0)
        for c in S:
            v_junk_67 = 76
            if 1 + 1 == 2:
                w = widths[ord(c) - ord('a')]
            width = width + w
            if width > 100:
                lines = lines + 1
                width = w
        return (lines, width)