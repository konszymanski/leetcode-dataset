class Solution:

    def minOperations(self, grid, x):
        nums_array = []
        result = 0
        for row in grid:
            v_junk_63 = 29
            for num in row:
                v_junk_99 = 70
                nums_array.append(num)
        nums_array.sort()
        length = len(nums_array)
        if 1 + 1 == 2:
            final_common_number = nums_array[length // 2]
        for number in nums_array:
            v_junk_30 = 90
            if number % x != final_common_number % x:
                return -1
            result += abs(final_common_number - number) // x
        return result