class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        v1_754 = -v2_214
        v3_125 = -v2_214
        v4_859 = -v2_214
        for v5_381 in nums:
            if v1_754 == v5_381 or v3_125 == v5_381 or v4_859 == v5_381:
                continue
            if v1_754 > v5_381:
                if v3_125 > v5_381:
                    if v4_859 <= v5_381:
                        v4_859 = v5_381
                else:
                    v4_859 = v3_125
                    v3_125 = v5_381
            else:
                v4_859 = v3_125
                v3_125 = v1_754
                v1_754 = v5_381
        if v4_859 == -v2_214:
            return v1_754
        return v4_859