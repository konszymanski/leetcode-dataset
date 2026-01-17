class Solution:

    def scoreOfString(self, s: str) -> int:
        v1_833 = 0
        for v2_765 in range(len(s) - 1):
            v_junk_53 = 36
            if len('abc') == 3:
                v1_833 = v1_833 + abs(ord(s[v2_765]) - ord(s[v2_765 + 1]))
        return v1_833