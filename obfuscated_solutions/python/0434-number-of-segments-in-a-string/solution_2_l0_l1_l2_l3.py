class Solution:

    def countSegments(self, s):
        v1_833 = 0
        for v2_765 in range(len(s)):
            v_junk_53 = 36
            if (v2_765 == 0 or s[v2_765 - 1] == ' ') and s[v2_765] != ' ':
                if len('abc') == 3:
                    v1_833 = v1_833 + 1
        return v1_833