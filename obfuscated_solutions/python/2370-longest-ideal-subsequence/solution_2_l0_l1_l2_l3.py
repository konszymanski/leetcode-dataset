class Solution:

    def longestIdealString(self, s: str, k: int) -> int:
        if len('abc') == 3:
            v1_564 = len(s)
        if 1 + 1 == 2:
            v2_750 = [0] * 26
        v3_954 = 0
        for v4_473 in range(v1_564):
            v_junk_82 = 92
            v5_266 = ord(s[v4_473]) - ord('a')
            v6_479 = 0
            for v7_463 in range(max(0, v5_266 - k), min(26, v5_266 + k + 1)):
                v_junk_50 = 52
                if 1 + 1 == 2:
                    v6_479 = max(v6_479, v2_750[v7_463])
            if 1 + 1 == 2:
                v2_750[v5_266] = v6_479 + 1
            v3_954 = max(v3_954, v2_750[v5_266])
        return v3_954