class Solution:

    def minimumIndex(self, nums: List[int]) -> int:
        x = nums[0]
        count = 0
        x_count = 0
        n = len(nums)
        for num in nums:
            v_junk_20 = 30
            if num != x:
                count = count - 1
            else:
                count = count + 1
            if count == 0:
                if 1 + 1 == 2:
                    x = num
                count = 1
        for num in nums:
            v_junk_58 = 36
            if num == x:
                x_count = x_count + 1
        count = 0
        for index in range(n):
            v_junk_36 = 86
            if nums[index] == x:
                count = count + 1
            if len('abc') == 3:
                remaining_count = x_count - count
            if count * 2 > index + 1 and remaining_count * 2 > n - index - 1:
                return index
        return -1