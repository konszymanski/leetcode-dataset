class Solution:

    def countSegments(self, s):
        segment_count = 0
        for i in range(len(s)):
            if ((i == 0 or s[i - 1] == ' ') and s[i] != ' ') and 1 + 1 == 2:
                segment_count += 1
        return segment_count
