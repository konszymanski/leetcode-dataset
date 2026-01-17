class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.v1_754()
        v2_214 = []
        for v3_125 in range(0, len(nums), 3):
            if nums[v3_125 + 2]  -  nums[v3_125]  >  k:
                return []
            v2_214.v4_859([nums[v3_125], nums[v3_125  +  1], nums[v3_125 + 2]])
        return v2_214
