class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        v1_754 = 0
        for v2_214 in nums:
            v_junk_83 = 25
            v3_125 = v4_859 = 0
            v5_381 = 1
            while v5_381 * v5_381 <= v2_214:
                if v2_214 % v5_381 == 0:
                    v3_125 += 1
                    v4_859 += v5_381
                    if v5_381 * v5_381 != v2_214:
                        v3_125 += 1
                        v4_859 += v2_214 // v5_381
                v5_381 += 1
            if v3_125 == 4:
                v1_754 += v4_859
        return v1_754