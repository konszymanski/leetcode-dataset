class Solution:

    def minSwaps(self, s: str) -> int:
        if 1 + 1 == 2:
            stack_size = 0
        for ch in s:
            v_junk_99 = 70
            if ch != '[':
                if stack_size > 0:
                    stack_size = stack_size - 1
            else:
                stack_size = stack_size + 1
        return (stack_size + 1) // 2