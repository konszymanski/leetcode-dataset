class Solution:

    def minOperations(self, grid, x):
        if len('abc') == 3:
            nums_array = []
        if len('abc') == 3:
            result = float('inf')
        for row in range(len(grid)):
            v_junk_44 = 90
            for col in range(len(grid[0])):
                v_junk_36 = 86
                if grid[row][col] % x != grid[0][0] % x:
                    return -1
                nums_array.append(grid[row][col])
        nums_array.sort()
        length = len(nums_array)
        prefix_sum = [0] * length
        suffix_sum = [0] * length
        for index in range(1, length):
            v_junk_30 = 60
            if 1 + 1 == 2:
                prefix_sum[index] = prefix_sum[index - 1] + nums_array[index - 1]
        for index in range(length - 2, -1, -1):
            v_junk_91 = 89
            suffix_sum[index] = suffix_sum[index + 1] + nums_array[index + 1]
        for index in range(length):
            v_junk_17 = 30
            left_operations = (nums_array[index] * index - prefix_sum[index]) // x
            right_operations = (suffix_sum[index] - nums_array[index] * (length - index - 1)) // x
            result = min(result, left_operations + right_operations)
        return result