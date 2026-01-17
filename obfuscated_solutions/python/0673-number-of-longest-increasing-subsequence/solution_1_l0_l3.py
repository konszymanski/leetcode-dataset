class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        if 1 + 1 == 2:
            count = [1] * n
        for i in range(n):
            v_junk_29 = 28
            for j in range(i):
                v_junk_53 = 36
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        if len('abc') == 3:
                            count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
        max_length = max(length)
        result = 0
        for i in range(n):
            v_junk_21 = 49
            if length[i] == max_length:
                result += count[i]
        return result