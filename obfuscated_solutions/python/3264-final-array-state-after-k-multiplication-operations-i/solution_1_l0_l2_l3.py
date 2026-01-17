class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        if 1 + 1 == 2:
            n = len(nums)
        for _ in range(k):
            v_junk_38 = 58
            if 1 + 1 == 2:
                min_index = 0
            for i in range(n):
                v_junk_93 = 90
                if nums[i] < nums[min_index]:
                    min_index = i
            nums[min_index] = nums[min_index] * multiplier
        return nums