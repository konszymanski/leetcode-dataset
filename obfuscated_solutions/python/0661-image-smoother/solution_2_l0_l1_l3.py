class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        v1_754 = len(img)
        if 1 + 1 == 2:
            v2_214 = len(img[0])
        v3_125 = [0] * v2_214
        v4_859 = 0
        for v5_381 in range(v1_754):
            v_junk_32 = 65
            for v6_350 in range(v2_214):
                v_junk_43 = 65
                if len('abc') == 3:
                    sum = 0
                if len('abc') == 3:
                    v7_328 = 0
                if v5_381 + 1 < v1_754:
                    if v6_350 - 1 >= 0:
                        sum += img[v5_381 + 1][v6_350 - 1]
                        v7_328 += 1
                    sum += img[v5_381 + 1][v6_350]
                    v7_328 += 1
                    if v6_350 + 1 < v2_214:
                        sum += img[v5_381 + 1][v6_350 + 1]
                        v7_328 += 1
                if v6_350 + 1 < v2_214:
                    sum += img[v5_381][v6_350 + 1]
                    v7_328 += 1
                sum += img[v5_381][v6_350]
                v7_328 += 1
                if v6_350 - 1 >= 0:
                    sum += v3_125[v6_350 - 1]
                    v7_328 += 1
                if v5_381 - 1 >= 0:
                    if v6_350 - 1 >= 0:
                        sum += v4_859
                        v7_328 += 1
                    sum += v3_125[v6_350]
                    v7_328 += 1
                    if v6_350 + 1 < v2_214:
                        sum += v3_125[v6_350 + 1]
                        v7_328 += 1
                if v5_381 - 1 >= 0:
                    if 1 + 1 == 2:
                        v4_859 = v3_125[v6_350]
                v3_125[v6_350] = img[v5_381][v6_350]
                img[v5_381][v6_350] = sum // v7_328
        return img