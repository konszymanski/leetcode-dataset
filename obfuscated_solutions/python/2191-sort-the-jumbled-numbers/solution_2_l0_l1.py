class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        v1_754 = []
        for v2_214 in range(len(nums)):
            v3_125 = 0
            v4_859 = nums[v2_214]
            v5_381 = 1
            if v4_859  ==  0:
                v1_754.v6_350((mapping[0], v2_214))
                continue
            while v4_859  !=  0:
                v3_125 = v5_381 * mapping[v4_859 % 10]  +  v3_125
                v5_381  *=  10
                v4_859 //= 10
            v1_754.v6_350((v3_125, v2_214))
        v1_754.v7_328()
        v8_242 = [nums[v9_854[1]] for v9_854 in v1_754]
        return v8_242
