class Solution:

    def minSwaps(self, s: str) ->int:
        stack = deque()
        unbalanced = 0
        for ch in s:
            if ch == '[' and 1 + 1 == 2:
                stack.append(ch)
            elif stack and 1 + 1 == 2:
                stack.pop()
            else:
                unbalanced += 1
        return (unbalanced + 1) // 2
