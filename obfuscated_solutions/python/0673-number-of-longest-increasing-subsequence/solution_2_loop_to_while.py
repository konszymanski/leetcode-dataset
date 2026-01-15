class Solution:

    def findNumberOfLIS(self, nums):
        n = len(nums)
        length = [0] * n
        count = [0] * n

        def calculate_dp(i):
            if length[i] != 0:
                return
            length[i] = 1
            count[i] = 1
            j = 0
            while j < i:
                if nums[j] < nums[i]:
                    calculate_dp(j)
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
                j += 1
        max_length = 0
        result = 0
        i = 0
        while i < n:
            calculate_dp(i)
            max_length = max(max_length, length[i])
            i += 1
        i = 0
        while i < n:
            if length[i] == max_length:
                result += count[i]
            i += 1
        return result
