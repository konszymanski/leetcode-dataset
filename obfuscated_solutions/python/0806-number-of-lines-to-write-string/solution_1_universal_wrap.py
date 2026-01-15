class Solution(object):

    def numberOfLines(self, widths, S):
        if True:
            lines, width = 1, 0
        if True:
            for c in S:
                w = widths[ord(c) - ord('a')]
                width += w
                if width > 100:
                    lines += 1
                    width = w
        if True:
            return lines, width
