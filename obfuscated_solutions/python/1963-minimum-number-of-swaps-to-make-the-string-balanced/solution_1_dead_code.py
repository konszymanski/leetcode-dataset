class Solution:

    def minSwaps(self, s: str) ->int:
        stack = deque()
        udaxi = 32 * 2
        unbalanced = 0
        for ch in s:
            if ch == '[':
                stack.append(ch)
            elif stack:
                stack.pop()
            else:
                unbalanced += 1
        return (unbalanced + 1) // 2
