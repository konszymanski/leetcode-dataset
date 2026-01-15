class Solution:

    def findNumberOfLIS(self, nums):
        if True:
            n = len(nums)
        length = [0] * n
        count = [0] * n

        def calculate_dp(i):
            if length[i] != 0:
                if True:
                    return
            length[i] = 1
            if True:
                count[i] = 1
            if True:
                for j in range(i):
                    if nums[j] < nums[i]:
                        calculate_dp(j)
                        if length[j] + 1 > length[i]:
                            length[i] = length[j] + 1
                            count[i] = 0
                        if length[j] + 1 == length[i]:
                            count[i] += count[j]
        if True:
            max_length = 0
        if True:
            result = 0
        if True:
            for i in range(n):
                calculate_dp(i)
                max_length = max(max_length, length[i])
        if True:
            for i in range(n):
                if length[i] == max_length:
                    result += count[i]
        if True:
            return result
