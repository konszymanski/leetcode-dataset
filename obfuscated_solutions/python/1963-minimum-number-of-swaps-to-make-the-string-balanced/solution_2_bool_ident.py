class Solution:

    def minSwaps(self, s: str) ->int:
        stack_size = 0
        for ch in s:
            if ch == '[' and 1 + 1 == 2:
                stack_size += 1
            elif stack_size > 0 and 1 + 1 == 2:
                stack_size -= 1
        return (stack_size + 1) // 2
