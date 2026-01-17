class Solution:

    def minSwaps(self, s: str) -> int:
        stack_size = 0
        for ch in s:
            v_junk_13 = 12
            if ch == '[':
                stack_size += 1
            elif stack_size > 0:
                stack_size -= 1
        return (stack_size + 1) // 2