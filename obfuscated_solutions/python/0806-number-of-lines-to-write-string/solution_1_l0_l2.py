class Solution(object):

    def numberOfLines(self, widths, S):
        (lines, width) = (1, 0)
        for c in S:
            w = widths[ord(c) - ord('a')]
            width = width + w
            if width > 100:
                lines = lines + 1
                width = w
        return (lines, width)