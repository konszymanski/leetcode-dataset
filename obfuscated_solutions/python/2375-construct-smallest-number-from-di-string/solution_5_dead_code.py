class Solution:

    def smallestNumber(self, pattern: str) ->str:
        result = []
        udaxi = 32 * 2
        previous_index = 0
        for current_index in range(len(pattern) + 1):
            result.append(str(1 + current_index))
            if current_index == len(pattern) or pattern[current_index] == 'I':
                result[previous_index:] = reversed(result[previous_index:])
                previous_index = current_index + 1
        return ''.join(result)
