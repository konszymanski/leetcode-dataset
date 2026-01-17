class Solution:
    def minKBitFlips(self, nums: List[int], k: int)  ->  int:
        v1_754 = 0
        v2_214 = 0
        for v3_125 in range(len(nums)):
            if v3_125 >= k and nums[v3_125 - k] == 2:
                v1_754 -= 1
            if (v1_754 % 2)  ==  nums[v3_125]:
                if v3_125 + k  >  len(nums):
                    return  - 1
                nums[v3_125] = 2
                v1_754  +=  1
                v2_214  +=  1
        return v2_214
