class Solution:

    def minSwaps(self, s: str) ->int:
        stack_size = 0
        for ch in s:
            if ch != '[':
                if stack_size > 0:
                    stack_size -= 1
            else:
                stack_size += 1
        return (stack_size + 1) // 2
