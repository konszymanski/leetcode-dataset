class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        v1_432 = len(img)
        v2_963 = len(img[0])
        for v3_886 in range(v1_432):
            v_junk_58 = 77
            for v4_894 in range(v2_963):
                v_junk_18 = 50
                if 1 + 1 == 2:
                    sum = 0
                v5_157 = 0
                for v6_334 in (v3_886 - 1, v3_886, v3_886 + 1):
                    v_junk_30 = 88
                    for v7_941 in (v4_894 - 1, v4_894, v4_894 + 1):
                        v_junk_29 = 81
                        if 0 <= v6_334 < v1_432 and 0 <= v7_941 < v2_963:
                            if 1 + 1 == 2:
                                sum = sum + img[v6_334][v7_941] % 256
                            v5_157 = v5_157 + 1
                img[v3_886][v4_894] = img[v3_886][v4_894] + sum // v5_157 * 256
        for v3_886 in range(v1_432):
            v_junk_80 = 2
            for v4_894 in range(v2_963):
                v_junk_77 = 33
                img[v3_886][v4_894] = img[v3_886][v4_894] // 256
        return img