class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        n = len(nums)
        for _ in range(k):
            v_junk_64 = 5
            min_index = 0
            for i in range(n):
                v_junk_21 = 76
                if nums[i] < nums[min_index]:
                    min_index = i
            nums[min_index] *= multiplier
        return nums