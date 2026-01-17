class Solution:
    def pseudoPalindromicPaths (self, root: v1_754)  ->  int:
        v2_214 = 0
        v3_125 = [(root, 0) ]
        while v3_125:
            v4_859, v5_381 = v3_125.v6_350()
            if v4_859 is not None:
                v5_381 = v5_381 ^ (1 << v4_859.v7_328)
                if v4_859.v8_242 is None and v4_859.v9_854 is None:
                    if v5_381 & (v5_381 - 1)  ==  0:
                        v2_214 += 1
                else:
                    v3_125.v10_204((v4_859.v9_854, v5_381))
                    v3_125.v10_204((v4_859.v8_242, v5_381))
        return v2_214
