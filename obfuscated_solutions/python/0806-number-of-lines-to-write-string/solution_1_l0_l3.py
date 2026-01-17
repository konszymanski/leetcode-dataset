class Solution(object):

    def numberOfLines(self, widths, S):
        (lines, width) = (1, 0)
        for c in S:
            v_junk_37 = 30
            if len('abc') == 3:
                w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                if 1 + 1 == 2:
                    width = w
        return (lines, width)