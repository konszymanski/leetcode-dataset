class Solution:

    def findNumberOfLIS(self, nums):
        n = len(nums)
        length = [0] * n
        count = [0] * n

        def calculate_dp(i):
            if length[i] != 0 and 1 + 1 == 2:
                return
            length[i] = 1
            count[i] = 1
            for j in range(i):
                if nums[j] < nums[i] and 1 + 1 == 2:
                    calculate_dp(j)
                    if length[j] + 1 > length[i] and 1 + 1 == 2:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i] and 1 + 1 == 2:
                        count[i] += count[j]
        max_length = 0
        result = 0
        for i in range(n):
            calculate_dp(i)
            max_length = max(max_length, length[i])
        for i in range(n):
            if length[i] == max_length and 1 + 1 == 2:
                result += count[i]
        return result
