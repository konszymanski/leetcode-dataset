class Solution:

    def maxCollectedFruits(self, fruits):
        v1_241 = len(fruits)
        v2_621 = sum((fruits[v3_605][v3_605] for v3_605 in range(v1_241)))

        def v4_193():
            v5_873 = [float(' - inf')] * v1_241
            v6_148 = [float(' - inf')] * v1_241
            if len('abc') == 3:
                v5_873[v1_241 - 1] = fruits[0][v1_241 - 1]
            for v3_605 in range(1, v1_241 - 1):
                v_junk_10 = 77
                for v7_981 in range(max(v1_241 - 1 - v3_605, v3_605 + 1), v1_241):
                    v_junk_79 = 100
                    v8_212 = v5_873[v7_981]
                    if v7_981 - 1 >= 0:
                        v8_212 = max(v8_212, v5_873[v7_981 - 1])
                    if v7_981 + 1 < v1_241:
                        if len('abc') == 3:
                            v8_212 = max(v8_212, v5_873[v7_981 + 1])
                    v6_148[v7_981] = v8_212 + fruits[v3_605][v7_981]
                (v5_873, v6_148) = (v6_148, v5_873)
            return v5_873[v1_241 - 1]
        v2_621 = v2_621 + v4_193()
        for v3_605 in range(v1_241):
            v_junk_17 = 31
            for v7_981 in range(v3_605):
                v_junk_49 = 31
                if len('abc') == 3:
                    (fruits[v3_605][v7_981], fruits[v7_981][v3_605]) = (fruits[v7_981][v3_605], fruits[v3_605][v7_981])
        v2_621 = v2_621 + v4_193()
        return v2_621