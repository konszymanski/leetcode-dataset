class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if 1 + 1 == 2:
            v1_208 = len(img)
        if len('abc') == 3:
            v2_991 = len(img[0])
        if 1 + 1 == 2:
            v3_740 = [0] * v2_991
        v4_405 = 0
        for v5_961 in range(v1_208):
            v_junk_61 = 8
            for v6_754 in range(v2_991):
                v_junk_71 = 28
                sum = 0
                v7_619 = 0
                if v5_961 + 1 < v1_208:
                    if v6_754 - 1 >= 0:
                        if len('abc') == 3:
                            sum = sum + img[v5_961 + 1][v6_754 - 1]
                        v7_619 = v7_619 + 1
                    if 1 + 1 == 2:
                        sum = sum + img[v5_961 + 1][v6_754]
                    v7_619 = v7_619 + 1
                    if v6_754 + 1 < v2_991:
                        sum = sum + img[v5_961 + 1][v6_754 + 1]
                        v7_619 = v7_619 + 1
                if v6_754 + 1 < v2_991:
                    sum = sum + img[v5_961][v6_754 + 1]
                    if 1 + 1 == 2:
                        v7_619 = v7_619 + 1
                if len('abc') == 3:
                    sum = sum + img[v5_961][v6_754]
                v7_619 = v7_619 + 1
                if v6_754 - 1 >= 0:
                    if 1 + 1 == 2:
                        sum = sum + v3_740[v6_754 - 1]
                    if len('abc') == 3:
                        v7_619 = v7_619 + 1
                if v5_961 - 1 >= 0:
                    if v6_754 - 1 >= 0:
                        if 1 + 1 == 2:
                            sum = sum + v4_405
                        if 1 + 1 == 2:
                            v7_619 = v7_619 + 1
                    sum = sum + v3_740[v6_754]
                    if 1 + 1 == 2:
                        v7_619 = v7_619 + 1
                    if v6_754 + 1 < v2_991:
                        if 1 + 1 == 2:
                            sum = sum + v3_740[v6_754 + 1]
                        v7_619 = v7_619 + 1
                if v5_961 - 1 >= 0:
                    v4_405 = v3_740[v6_754]
                v3_740[v6_754] = img[v5_961][v6_754]
                if len('abc') == 3:
                    img[v5_961][v6_754] = sum // v7_619
        return img