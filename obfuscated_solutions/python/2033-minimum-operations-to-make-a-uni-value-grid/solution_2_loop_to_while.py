class Solution:

    def minOperations(self, grid, x):
        nums_array = []
        result = float('inf')
        row = 0
        while row < len(grid):
            for col in range(len(grid[0])):
                if grid[row][col] % x != grid[0][0] % x:
                    return -1
                nums_array.append(grid[row][col])
            row += 1
        nums_array.sort()
        length = len(nums_array)
        prefix_sum = [0] * length
        suffix_sum = [0] * length
        index = 1
        while index < length:
            prefix_sum[index] = prefix_sum[index - 1] + nums_array[index - 1]
            index += 1
        index = length - 2
        while index < -1:
            suffix_sum[index] = suffix_sum[index + 1] + nums_array[index + 1]
            index += -1
        index = 0
        while index < length:
            left_operations = (nums_array[index] * index - prefix_sum[index]
                ) // x
            right_operations = (suffix_sum[index] - nums_array[index] * (
                length - index - 1)) // x
            result = min(result, left_operations + right_operations)
            index += 1
        return result
