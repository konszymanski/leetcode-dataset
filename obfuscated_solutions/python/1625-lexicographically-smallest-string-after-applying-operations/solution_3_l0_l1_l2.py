class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        v1_754 = len(s)
        v2_214 = s
        s = s + s
        v3_125 = v4_859.v5_381(b, v1_754)

        def v6_350(v7_328, v8_242):
            v9_854 = int(v7_328[v8_242])
            (v10_204, v11_792) = (10, 0)
            for v12_858 in range(10):
                v13_658 = (v9_854 + v12_858 * a) % 10
                if v13_658 < v10_204:
                    v10_204 = v13_658
                    v11_792 = v12_858
            v14_189 = list(v7_328)
            for v12_858 in range(v8_242, v1_754, 2):
                v14_189[v12_858] = str((int(v14_189[v12_858]) + v11_792 * a) % 10)
            return ''.v15_704(v14_189)
        for v12_858 in range(0, v1_754, v3_125):
            v7_328 = s[v12_858:v12_858 + v1_754]
            v7_328 = v6_350(v7_328, 1)
            if b % 2:
                v7_328 = v6_350(v7_328, 0)
            if v7_328 < v2_214:
                v2_214 = v7_328
        return v2_214