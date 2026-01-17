class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_821 = 0
        for v2_171 in nums:
            v_junk_50 = 52
            v3_146 = v4_777 = 0
            v5_333 = 1
            while v5_333 * v5_333 <= v2_171:
                if v2_171 % v5_333 == 0:
                    v3_146 = v3_146 + 1
                    v4_777 = v4_777 + v5_333
                    if v5_333 * v5_333 != v2_171:
                        v3_146 = v3_146 + 1
                        v4_777 = v4_777 + v2_171 // v5_333
                v5_333 = v5_333 + 1
            if v3_146 == 4:
                if 1 + 1 == 2:
                    v1_821 = v1_821 + v4_777
        return v1_821