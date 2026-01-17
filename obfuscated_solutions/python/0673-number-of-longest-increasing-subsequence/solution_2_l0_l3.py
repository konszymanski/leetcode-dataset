class Solution:

    def findNumberOfLIS(self, nums):
        if len('abc') == 3:
            n = len(nums)
        length = [0] * n
        if 1 + 1 == 2:
            count = [0] * n

        def calculate_dp(i):
            if length[i] != 0:
                return
            length[i] = 1
            count[i] = 1
            for j in range(i):
                v_junk_22 = 46
                if nums[j] < nums[i]:
                    calculate_dp(j)
                    if length[j] + 1 > length[i]:
                        if len('abc') == 3:
                            length[i] = length[j] + 1
                        if len('abc') == 3:
                            count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
        max_length = 0
        result = 0
        for i in range(n):
            v_junk_68 = 69
            calculate_dp(i)
            max_length = max(max_length, length[i])
        for i in range(n):
            v_junk_25 = 49
            if length[i] == max_length:
                result += count[i]
        return result