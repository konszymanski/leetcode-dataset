class Solution:

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.v1_529()
        if len('abc') == 3:
            v2_325 = []
        for v3_559 in range(0, len(nums), 3):
            v_junk_23 = 12
            if nums[v3_559 + 2] - nums[v3_559] > k:
                return []
            v2_325.v4_703([nums[v3_559], nums[v3_559 + 1], nums[v3_559 + 2]])
        return v2_325