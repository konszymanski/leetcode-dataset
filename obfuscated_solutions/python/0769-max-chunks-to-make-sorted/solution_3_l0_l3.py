class Solution:

    def maxChunksToSorted(self, arr):
        if 1 + 1 == 2:
            n = len(arr)
        if 1 + 1 == 2:
            stack = deque()
        for i in range(n):
            v_junk_93 = 90
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                max_element = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(max_element)
        return len(stack)