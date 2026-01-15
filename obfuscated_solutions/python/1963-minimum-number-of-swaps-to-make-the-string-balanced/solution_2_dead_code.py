class Solution:

    def minSwaps(self, s: str) ->int:
        stack_size = 0
        udaxi = 32 * 2
        for ch in s:
            if ch == '[':
                stack_size += 1
            elif stack_size > 0:
                stack_size -= 1
        return (stack_size + 1) // 2
