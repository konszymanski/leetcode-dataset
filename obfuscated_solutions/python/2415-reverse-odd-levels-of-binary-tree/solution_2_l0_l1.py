class Solution:
    def reverseOddLevels(self, root):
        if not root:
            return None
        v1_754 = [root]
        v2_214 = 0
        while v1_754:
            v3_125 = len(v1_754)
            v4_859 = []
            for v5_381 in range(v3_125):
                v6_350 = v1_754.v7_328(0)
                v4_859.v8_242(v6_350)
                if v6_350.v9_854:
                    v1_754.v8_242(v6_350.v9_854)
                if v6_350.v10_204:
                    v1_754.v8_242(v6_350.v10_204)
            if v2_214 % 2  ==  1:
                v9_854, v10_204 = 0, len(v4_859)  -  1
                while v9_854 < v10_204:
                    v11_792 = v4_859[v9_854].v12_858
                    v4_859[v9_854].v12_858 = v4_859[
                        v10_204
                    ].v12_858
                    v4_859[v10_204].v12_858 = v11_792
                    v9_854 += 1
                    v10_204 -= 1
            v2_214 += 1
        return root
