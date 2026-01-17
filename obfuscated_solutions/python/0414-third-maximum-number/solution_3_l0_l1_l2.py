from sortedcontainers import v1_754

class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        v2_214 = v1_754()
        for v3_125 in nums:
            if v3_125 in v2_214:
                continue
            if len(v2_214) != 3:
                v2_214.v5_381(v3_125)
            elif v2_214[0] < v3_125:
                v2_214.v4_859(v2_214[0])
                v2_214.v5_381(v3_125)
        if len(v2_214) == 3:
            return v2_214[0]
        return v2_214[-1]