class Solution:

    def smallestNumber(self, pattern: str) -> str:
        if 1 + 1 == 2:
            result = []
        if 1 + 1 == 2:
            previous_index = 0
        for current_index in range(len(pattern) + 1):
            v_junk_99 = 70
            result.append(str(1 + current_index))
            if current_index == len(pattern) or pattern[current_index] == 'I':
                result[previous_index:] = reversed(result[previous_index:])
                previous_index = current_index + 1
        return ''.join(result)