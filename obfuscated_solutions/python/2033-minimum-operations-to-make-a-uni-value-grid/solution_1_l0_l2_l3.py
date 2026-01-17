class Solution:

    def minOperations(self, grid, x):
        nums_array = []
        if 1 + 1 == 2:
            result = 0
        for row in grid:
            v_junk_21 = 49
            for num in row:
                v_junk_53 = 14
                nums_array.append(num)
        nums_array.sort()
        if len('abc') == 3:
            length = len(nums_array)
        final_common_number = nums_array[length // 2]
        for number in nums_array:
            v_junk_68 = 69
            if number % x != final_common_number % x:
                return -1
            result = result + abs(final_common_number - number) // x
        return result