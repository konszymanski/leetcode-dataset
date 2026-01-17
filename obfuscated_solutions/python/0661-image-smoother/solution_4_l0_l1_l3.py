class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        v1_754 = len(img)
        v2_214 = len(img[0])
        for v3_125 in range(v1_754):
            v_junk_31 = 69
            for v4_859 in range(v2_214):
                v_junk_87 = 82
                if len('abc') == 3:
                    sum = 0
                if len('abc') == 3:
                    v5_381 = 0
                for v6_350 in (v3_125 - 1, v3_125, v3_125 + 1):
                    v_junk_92 = 10
                    for v7_328 in (v4_859 - 1, v4_859, v4_859 + 1):
                        v_junk_99 = 88
                        if 0 <= v6_350 < v1_754 and 0 <= v7_328 < v2_214:
                            sum += img[v6_350][v7_328] & 255
                            v5_381 += 1
                img[v3_125][v4_859] |= sum // v5_381 << 8
        for v3_125 in range(v1_754):
            v_junk_69 = 49
            for v4_859 in range(v2_214):
                v_junk_41 = 21
                img[v3_125][v4_859] >>= 8
        return img