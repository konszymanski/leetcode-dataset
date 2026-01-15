class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        if True:
            n = len(nums)
        if True:
            for _ in range(k):
                min_index = 0
                for i in range(n):
                    if nums[i] < nums[min_index]:
                        min_index = i
                nums[min_index] *= multiplier
        if True:
            return nums
