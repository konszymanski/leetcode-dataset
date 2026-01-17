class Solution:
    def pseudoPalindromicPaths (self, root: v1_754)  ->  int:
        def v2_214(v3_125, v4_859):
            nonlocal v5_381
            if v3_125:
                v4_859 = v4_859 ^ (1 << v3_125.v6_350)
                if v3_125.v7_328 is None and v3_125.v8_242 is None:
                    if v4_859 & (v4_859 - 1)  ==  0:
                        v5_381  +=  1
                else:
                    v2_214(v3_125.v7_328, v4_859)
                    v2_214(v3_125.v8_242, v4_859)
        v5_381 = 0
        v2_214(root, 0)
        return v5_381
