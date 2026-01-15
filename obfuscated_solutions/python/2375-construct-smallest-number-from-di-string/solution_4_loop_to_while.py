class Solution:

    def smallestNumber(self, pattern: str) ->str:
        result = []
        num_stack = []
        index = 0
        while index < len(pattern) + 1:
            num_stack.append(index + 1)
            if index == len(pattern) or pattern[index] == 'I':
                while num_stack:
                    result.append(str(num_stack.pop()))
            index += 1
        return ''.join(result)
