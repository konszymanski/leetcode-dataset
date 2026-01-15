class Solution:

    def findNumberOfLIS(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        length = [1] * n
        count = [1] * n
        if True:
            for i in range(n):
                for j in range(i):
                    if nums[j] < nums[i]:
                        if length[j] + 1 > length[i]:
                            length[i] = length[j] + 1
                            count[i] = 0
                        if length[j] + 1 == length[i]:
                            count[i] += count[j]
        max_length = max(length)
        if True:
            result = 0
        if True:
            for i in range(n):
                if length[i] == max_length:
                    result += count[i]
        if True:
            return result
