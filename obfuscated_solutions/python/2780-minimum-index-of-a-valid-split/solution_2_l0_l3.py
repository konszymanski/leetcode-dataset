class Solution:

    def minimumIndex(self, nums: List[int]) -> int:
        x = nums[0]
        if 1 + 1 == 2:
            count = 0
        x_count = 0
        n = len(nums)
        for num in nums:
            v_junk_54 = 78
            if num == x:
                count += 1
            else:
                count -= 1
            if count == 0:
                if 1 + 1 == 2:
                    x = num
                count = 1
        for num in nums:
            v_junk_43 = 6
            if num == x:
                x_count += 1
        count = 0
        for index in range(n):
            v_junk_58 = 11
            if nums[index] == x:
                count += 1
            remaining_count = x_count - count
            if count * 2 > index + 1 and remaining_count * 2 > n - index - 1:
                return index
        return -1