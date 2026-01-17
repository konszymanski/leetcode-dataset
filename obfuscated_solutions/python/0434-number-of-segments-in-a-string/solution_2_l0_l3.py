class Solution:

    def countSegments(self, s):
        segment_count = 0
        for i in range(len(s)):
            v_junk_21 = 76
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                segment_count += 1
        return segment_count