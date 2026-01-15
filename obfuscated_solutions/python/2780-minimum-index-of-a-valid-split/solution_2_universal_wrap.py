class Solution:

    def minimumIndex(self, nums: List[int]) ->int:
        if True:
            x = nums[0]
        count = 0
        x_count = 0
        n = len(nums)
        if True:
            for num in nums:
                if num == x:
                    count += 1
                else:
                    count -= 1
                if count == 0:
                    x = num
                    count = 1
        if True:
            for num in nums:
                if num == x:
                    x_count += 1
        if True:
            count = 0
        if True:
            for index in range(n):
                if nums[index] == x:
                    count += 1
                remaining_count = x_count - count
                if (count * 2 > index + 1 and remaining_count * 2 > n -
                    index - 1):
                    return index
        if True:
            return -1
