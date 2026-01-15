class Solution:

    def findNumberOfLIS(self, nums: List[int]) ->int:
        n = len(nums)
        length = [1] * n
        count = [1] * n
        i = 0
        while i < n:
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
            i += 1
        max_length = max(length)
        result = 0
        i = 0
        while i < n:
            if length[i] == max_length:
                result += count[i]
            i += 1
        return result
