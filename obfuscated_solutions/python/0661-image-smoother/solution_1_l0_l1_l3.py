class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        v1_754 = len(img)
        v2_214 = len(img[0])
        v3_125 = [[0] * v2_214 for v4_859 in range(v1_754)]
        for v5_381 in range(v1_754):
            v_junk_41 = 21
            for v6_350 in range(v2_214):
                v_junk_31 = 69
                if len('abc') == 3:
                    sum = 0
                if len('abc') == 3:
                    v7_328 = 0
                for v8_242 in (v5_381 - 1, v5_381, v5_381 + 1):
                    v_junk_92 = 10
                    for v9_854 in (v6_350 - 1, v6_350, v6_350 + 1):
                        v_junk_99 = 88
                        if 0 <= v8_242 < v1_754 and 0 <= v9_854 < v2_214:
                            sum += img[v8_242][v9_854]
                            v7_328 += 1
                v3_125[v5_381][v6_350] = sum // v7_328
        return v3_125