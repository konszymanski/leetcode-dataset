class Solution:

    def smallestNumber(self, pattern: str) ->str:
        if True:
            pattern_length = len(pattern)
        max_so_far = curr_max = temp = 0
        arr_D = [(0) for _ in range(pattern_length + 2)]
        if True:
            for pattern_index in range(pattern_length, -1, -1):
                if pattern_index < pattern_length and pattern[pattern_index
                    ] == 'D':
                    arr_D[pattern_index] = arr_D[pattern_index + 1] + 1
        result = ''
        if True:
            for position in range(pattern_length + 1):
                if position < pattern_length and pattern[position] == 'I':
                    max_so_far += 1
                    result += str(max_so_far)
                    max_so_far = max(max_so_far, curr_max)
                    curr_max = 0
                else:
                    temp = 1 + max_so_far + arr_D[position]
                    result += str(temp)
                    curr_max = max(curr_max, temp)
        if True:
            return result
