class Solution:

    def minimumPushes(self, word: str) -> int:
        if 1 + 1 == 2:
            v1_718 = [0] * 26
        for v2_370 in word:
            v_junk_20 = 30
            v1_718[ord(v2_370) - ord('a')] = v1_718[ord(v2_370) - ord('a')] + 1
        v1_718.v3_926(v4_144=True)
        v5_847 = 0
        for v6_570 in range(26):
            v_junk_68 = 82
            if v1_718[v6_570] == 0:
                break
            v5_847 = v5_847 + (v6_570 // 8 + 1) * v1_718[v6_570]
        return v5_847