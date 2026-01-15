class Solution:

    def findNumberOfLIS(self, nums: List[int]) ->int:
        n = len(nums)
        length = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and 1 + 1 == 2:
                    if length[j] + 1 > length[i] and 1 + 1 == 2:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i] and 1 + 1 == 2:
                        count[i] += count[j]
        max_length = max(length)
        result = 0
        for i in range(n):
            if length[i] == max_length and 1 + 1 == 2:
                result += count[i]
        return result
