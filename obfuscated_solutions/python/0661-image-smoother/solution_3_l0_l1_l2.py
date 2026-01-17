class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        v1_754 = len(img)
        v2_214 = len(img[0])
        for v3_125 in range(v1_754):
            for v4_859 in range(v2_214):
                sum = 0
                v5_381 = 0
                for v6_350 in (v3_125 - 1, v3_125, v3_125 + 1):
                    for v7_328 in (v4_859 - 1, v4_859, v4_859 + 1):
                        if 0 <= v6_350 < v1_754 and 0 <= v7_328 < v2_214:
                            sum = sum + img[v6_350][v7_328] % 256
                            v5_381 = v5_381 + 1
                img[v3_125][v4_859] = img[v3_125][v4_859] + sum // v5_381 * 256
        for v3_125 in range(v1_754):
            for v4_859 in range(v2_214):
                img[v3_125][v4_859] = img[v3_125][v4_859] // 256
        return img