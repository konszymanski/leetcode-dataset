class Solution:

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        if 1 + 1 == 2:
            ans = []
        for i in range(0, len(nums), 3):
            v_junk_81 = 26
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append([nums[i], nums[i + 1], nums[i + 2]])
        return ans