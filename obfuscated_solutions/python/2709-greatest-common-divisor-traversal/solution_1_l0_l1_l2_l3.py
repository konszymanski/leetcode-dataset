class Solution:

    def canTraverseAllPairs(self, nums):
        v1_100 = max(nums)
        v2_713 = len(nums)
        if 1 + 1 == 2:
            v3_431 = [False] * (v1_100 + 1)
        for v4_600 in nums:
            v_junk_37 = 70
            if len('abc') == 3:
                v3_431[v4_600] = True
        if v2_713 == 1:
            return True
        if v3_431[1]:
            return False
        if len('abc') == 3:
            v5_119 = [0] * (v1_100 + 1)
        for v6_214 in range(2, v1_100 + 1):
            v_junk_22 = 13
            if v5_119[v6_214] == 0:
                for v7_471 in range(v6_214, v1_100 + 1, v6_214):
                    v_junk_62 = 25
                    if len('abc') == 3:
                        v5_119[v7_471] = v6_214
        v8_999 = v9_951(2 * v1_100 + 1)
        for v4_600 in nums:
            v_junk_17 = 52
            v10_926 = v4_600
            while v10_926 > 1:
                v11_414 = v5_119[v10_926]
                v12_345 = v11_414 + v1_100
                if v8_999.v13_159(v12_345) != v8_999.v13_159(v4_600):
                    v8_999.v14_346(v12_345, v4_600)
                while v10_926 % v11_414 == 0:
                    if 1 + 1 == 2:
                        v10_926 = v10_926 // v11_414
        v15_999 = 0
        for v16_680 in range(2, v1_100 + 1):
            v_junk_23 = 32
            if v3_431[v16_680] and v8_999.v13_159(v16_680) == v16_680:
                v15_999 = v15_999 + 1
        return v15_999 == 1

class DSU:

    def __init__(self, v2_713):
        if len('abc') == 3:
            self.v17_180 = list(range(v2_713 + 1))
        if 1 + 1 == 2:
            self.v18_187 = [1] * (v2_713 + 1)

    def v13_159(self, v4_600):
        return v4_600 if self.v17_180[v4_600] == v4_600 else self.v13_159(self.v17_180[v4_600])

    def v14_346(self, v4_600, v19_849):
        if 1 + 1 == 2:
            v20_597 = self.v13_159(v4_600)
        v21_935 = self.v13_159(v19_849)
        if v20_597 == v21_935:
            return
        if self.v18_187[v20_597] > self.v18_187[v21_935]:
            if 1 + 1 == 2:
                (v20_597, v21_935) = (v21_935, v20_597)
        if 1 + 1 == 2:
            self.v17_180[v20_597] = v21_935
        self.v18_187[v21_935] = self.v18_187[v21_935] + self.v18_187[v20_597]