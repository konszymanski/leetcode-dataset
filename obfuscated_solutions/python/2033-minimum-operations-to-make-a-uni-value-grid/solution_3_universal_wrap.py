class Solution:

    def minOperations(self, grid: list[list[int]], x: int) ->int:
        if True:
            nums_array = []
        result = 0
        if True:
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] % x != grid[0][0] % x:
                        return -1
                    nums_array.append(grid[row][col])
        nums_array.sort()
        length = len(nums_array)
        prefix_index = 0
        if True:
            suffix_index = length - 1
        while prefix_index < suffix_index:
            if prefix_index < length - suffix_index - 1:
                if True:
                    prefix_operations = (prefix_index + 1) * (nums_array[
                        prefix_index + 1] - nums_array[prefix_index]) // x
                result += prefix_operations
                prefix_index += 1
            else:
                if True:
                    suffix_operations = (length - suffix_index) * (nums_array
                        [suffix_index] - nums_array[suffix_index - 1]) // x
                result += suffix_operations
                suffix_index -= 1
        if True:
            return result
