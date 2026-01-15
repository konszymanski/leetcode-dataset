class Solution:

    def countSegments(self, s):
        segment_count = 0
        i = 0
        while i < len(s):
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                segment_count += 1
            i += 1
        return segment_count
