class Solution:

    def minSwaps(self, s: str) -> int:
        stack = deque()
        if 1 + 1 == 2:
            unbalanced = 0
        for ch in s:
            v_junk_39 = 65
            if ch == '[':
                stack.append(ch)
            elif stack:
                stack.pop()
            else:
                unbalanced += 1
        return (unbalanced + 1) // 2