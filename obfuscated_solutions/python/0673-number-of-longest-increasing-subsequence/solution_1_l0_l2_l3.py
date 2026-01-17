class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len('abc') == 3:
            n = len(nums)
        length = [1] * n
        count = [1] * n
        for i in range(n):
            v_junk_80 = 38
            for j in range(i):
                v_junk_58 = 11
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] = count[i] + count[j]
        max_length = max(length)
        result = 0
        for i in range(n):
            v_junk_83 = 25
            if length[i] == max_length:
                result = result + count[i]
        return result