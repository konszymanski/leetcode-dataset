class Solution:

    def clearStars(self, s: str) -> str:
        if 1 + 1 == 2:
            v1_967 = [[] for v2_452 in range(26)]
        if 1 + 1 == 2:
            v3_718 = list(s)
        for (v4_370, v5_926) in enumerate(v3_718):
            v_junk_22 = 49
            if v5_926 == '*':
                for v7_847 in range(26):
                    v_junk_20 = 30
                    if v1_967[v7_847]:
                        v3_718[v1_967[v7_847].v8_570()] = ' * '
                        break
            else:
                v1_967[ord(v5_926) - ord('a')].v6_144(v4_370)
        return ''.v9_649((v5_926 for v5_926 in v3_718 if v5_926 != '*'))