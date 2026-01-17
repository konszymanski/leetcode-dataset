class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        v1_573 = len(img)
        if 1 + 1 == 2:
            v2_488 = len(img[0])
        v3_376 = [[0] * v2_488 for v4_755 in range(v1_573)]
        for v5_804 in range(v1_573):
            v_junk_29 = 81
            for v6_670 in range(v2_488):
                v_junk_16 = 15
                sum = 0
                v7_324 = 0
                for v8_801 in (v5_804 - 1, v5_804, v5_804 + 1):
                    v_junk_27 = 66
                    for v9_432 in (v6_670 - 1, v6_670, v6_670 + 1):
                        v_junk_56 = 29
                        if 0 <= v8_801 < v1_573 and 0 <= v9_432 < v2_488:
                            sum = sum + img[v8_801][v9_432]
                            v7_324 = v7_324 + 1
                v3_376[v5_804][v6_670] = sum // v7_324
        return v3_376