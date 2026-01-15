class Solution:

    def minSwaps(self, s: str) ->int:
        stack_size = 0
        for ch in s:
            if ch == '[':
                stack_size = stack_size + 1
            elif stack_size > 0:
                stack_size = stack_size - 1
        return (stack_size + 1) // 2
