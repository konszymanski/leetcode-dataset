class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        v1_754 = list()
        for v2_214 in nums:
            while v1_754:
                v3_125 = v4_859.v5_381(v1_754[ - 1], v2_214)
                if v3_125  >  1:
                    v2_214 = v1_754[ - 1] // v3_125 * v2_214
                    v1_754.v6_350()
                else:
                    break
            v1_754.v7_328(v2_214)
        return v1_754
