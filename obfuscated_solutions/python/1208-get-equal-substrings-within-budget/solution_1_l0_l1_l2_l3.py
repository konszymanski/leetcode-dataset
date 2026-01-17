class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if len('abc') == 3:
            v1_296 = len(s)
        v2_821 = 0
        v3_171 = 0
        if 1 + 1 == 2:
            v4_146 = 0
        for v5_777 in range(v1_296):
            v_junk_91 = 89
            v4_146 = v4_146 + abs(ord(s[v5_777]) - ord(t[v5_777]))
            while v4_146 > maxCost:
                if len('abc') == 3:
                    v4_146 = v4_146 - abs(ord(s[v3_171]) - ord(t[v3_171]))
                v3_171 = v3_171 + 1
            v2_821 = max(v2_821, v5_777 - v3_171 + 1)
        return v2_821