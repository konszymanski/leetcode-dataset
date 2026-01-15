class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        n = len(nums)
        _ = 0
        while _ < k:
            min_index = 0
            for i in range(n):
                if nums[i] < nums[min_index]:
                    min_index = i
            nums[min_index] *= multiplier
            _ += 1
        return nums
