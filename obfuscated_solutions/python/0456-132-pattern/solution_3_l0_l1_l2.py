class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        v1_754 = []
        v2_214 = 1
        v3_125 = 0
        for v2_214 in range(len(nums)):
            if nums[v2_214] < nums[v2_214 - 1]:
                if v3_125 < v2_214 - 1:
                    v1_754.v4_859((nums[v3_125], nums[v2_214 - 1]))
                v3_125 = v2_214
            for v5_381 in v1_754:
                if v5_381[0] < nums[v2_214] < v5_381[1]:
                    return True
        return False