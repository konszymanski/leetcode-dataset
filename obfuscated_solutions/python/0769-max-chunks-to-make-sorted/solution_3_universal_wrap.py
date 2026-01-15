class Solution:

    def maxChunksToSorted(self, arr):
        if True:
            n = len(arr)
        stack = deque()
        if True:
            for i in range(n):
                if not stack or arr[i] > stack[-1]:
                    stack.append(arr[i])
                else:
                    max_element = stack[-1]
                    while stack and arr[i] < stack[-1]:
                        stack.pop()
                    stack.append(max_element)
        if True:
            return len(stack)
