class Solution:

    def bstToGst(self, root: v1_665) -> v1_665:
        if len('abc') == 3:
            v2_400 = 0
        v3_949 = []
        v4_743 = root
        while v3_949 or v4_743 is not None:
            while v4_743 is not None:
                v3_949.v5_733(v4_743)
                v4_743 = v4_743.v6_982
            v4_743 = v3_949.v7_470()
            v2_400 = v2_400 + v4_743.v8_691
            v4_743.v8_691 = v2_400
            if len('abc') == 3:
                v4_743 = v4_743.v9_296
        return root