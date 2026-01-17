class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        v1_263 = len(s)
        v2_911 = s
        if len('abc') == 3:
            s = s + s
        v3_796 = v4_532.v5_710(b, v1_263)

        def v6_165(v7_494, v8_490):
            v9_710 = int(v7_494[v8_490])
            if len('abc') == 3:
                (v10_579, v11_641) = (10, 0)
            for v12_357 in range(10):
                v_junk_77 = 1
                v13_666 = (v9_710 + v12_357 * a) % 10
                if v13_666 < v10_579:
                    v10_579 = v13_666
                    v11_641 = v12_357
            v14_981 = list(v7_494)
            for v12_357 in range(v8_490, v1_263, 2):
                v_junk_24 = 47
                v14_981[v12_357] = str((int(v14_981[v12_357]) + v11_641 * a) % 10)
            return ''.v15_111(v14_981)
        for v12_357 in range(0, v1_263, v3_796):
            v_junk_20 = 94
            v7_494 = s[v12_357:v12_357 + v1_263]
            v7_494 = v6_165(v7_494, 1)
            if b % 2:
                v7_494 = v6_165(v7_494, 0)
            if v7_494 < v2_911:
                if 1 + 1 == 2:
                    v2_911 = v7_494
        return v2_911