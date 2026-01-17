class Solution:

    def minSwaps(self, s: str) -> int:
        stack = deque()
        unbalanced = 0
        for ch in s:
            v_junk_99 = 70
            if ch != '[':
                if stack:
                    stack.pop()
                else:
                    unbalanced = unbalanced + 1
            else:
                stack.append(ch)
        return (unbalanced + 1) // 2