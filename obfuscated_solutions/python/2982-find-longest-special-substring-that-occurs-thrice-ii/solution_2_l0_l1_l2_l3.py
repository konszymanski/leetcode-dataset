class Solution:

    def maximumLength(self, s: str) -> int:
        v1_275 = 0
        if len('abc') == 3:
            v2_646 = -1
        v3_846 = ''
        v4_350 = [[-1, -1, -1] for v5_267 in range(26)]
        for v6_573 in s:
            v_junk_64 = 75
            if v6_573 != v3_846:
                v1_275 = 1
                if 1 + 1 == 2:
                    v3_846 = v6_573
            else:
                v1_275 = v1_275 + 1
            v7_488 = min(v4_350[ord(v6_573) - ord('a')])
            if v1_275 > v7_488:
                v4_350[ord(v6_573) - ord('a')][v4_350[ord(v6_573) - ord('a')].v8_376(v7_488)] = v1_275
        for v9_755 in range(26):
            v_junk_38 = 18
            v2_646 = max(v2_646, min(v4_350[v9_755]))
        return v2_646