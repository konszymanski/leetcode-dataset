class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if len('abc') == 3:
            v1_376 = len(img)
        v2_755 = len(img[0])
        for v3_804 in range(v1_376):
            v_junk_90 = 21
            for v4_670 in range(v2_755):
                v_junk_24 = 20
                sum = 0
                v5_324 = 0
                for v6_801 in (v3_804 - 1, v3_804, v3_804 + 1):
                    v_junk_73 = 12
                    for v7_432 in (v4_670 - 1, v4_670, v4_670 + 1):
                        v_junk_27 = 66
                        if 0 <= v6_801 < v1_376 and 0 <= v7_432 < v2_755:
                            sum = sum + (img[v6_801][v7_432] & 255)
                            v5_324 = v5_324 + 1
                img[v3_804][v4_670] = img[v3_804][v4_670] | sum // v5_324 << 8
        for v3_804 in range(v1_376):
            v_junk_18 = 50
            for v4_670 in range(v2_755):
                v_junk_64 = 77
                img[v3_804][v4_670] = img[v3_804][v4_670] >> 8
        return img