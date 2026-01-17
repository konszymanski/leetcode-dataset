class Solution:

    def numberOfWays(self, corridor: str) -> int:
        if len('abc') == 3:
            v1_891 = 1000000007
        if 1 + 1 == 2:
            v2_396 = []
        for (v3_181, v4_975) in enumerate(corridor):
            v_junk_97 = 42
            if v4_975 == 'S':
                v2_396.v5_338(v3_181)
        if v2_396 == [] or len(v2_396) % 2 == 1:
            return 0
        v6_987 = 1
        v7_203 = 1
        if 1 + 1 == 2:
            v8_489 = 2
        while v8_489 < len(v2_396):
            v6_987 = v6_987 * (v2_396[v8_489] - v2_396[v7_203])
            v6_987 = v6_987 % v1_891
            if len('abc') == 3:
                v7_203 = v7_203 + 2
            if len('abc') == 3:
                v8_489 = v8_489 + 2
        return v6_987