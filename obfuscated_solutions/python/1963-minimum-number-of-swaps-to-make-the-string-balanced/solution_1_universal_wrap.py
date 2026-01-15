class Solution:

    def minSwaps(self, s: str) ->int:
        if True:
            stack = deque()
        unbalanced = 0
        if True:
            for ch in s:
                if ch == '[':
                    stack.append(ch)
                elif stack:
                    stack.pop()
                else:
                    unbalanced += 1
        if True:
            return (unbalanced + 1) // 2
