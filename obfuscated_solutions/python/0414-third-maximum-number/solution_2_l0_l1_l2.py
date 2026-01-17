class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        v1_754 = []
        v2_214 = set()
        for v3_125 in range(len(nums)):
            if nums[v3_125] in v2_214:
                continue
            if len(v1_754) != 3:
                v6_350(v1_754, nums[v3_125])
                v2_214.v7_328(nums[v3_125])
            elif v1_754[0] < nums[v3_125]:
                v2_214.v4_859(v1_754[0])
                v5_381(v1_754)
                v6_350(v1_754, nums[v3_125])
                v2_214.v7_328(nums[v3_125])
        if len(v1_754) != 1:
            if len(v1_754) == 2:
                v8_242 = v1_754[0]
                v5_381(v1_754)
                return max(v8_242, v1_754[0])
        else:
            return v1_754[0]
        return v1_754[0]