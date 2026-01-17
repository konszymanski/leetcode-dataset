from sortedcontainers import v1_658

class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            v2_529 = v1_658()
        for v3_325 in nums:
            v_junk_53 = 14
            if v3_325 in v2_529:
                continue
            if len(v2_529) != 3:
                v2_529.v5_703(v3_325)
            elif v2_529[0] < v3_325:
                v2_529.v4_559(v2_529[0])
                v2_529.v5_703(v3_325)
        if len(v2_529) == 3:
            return v2_529[0]
        return v2_529[-1]