class Solution:

    def maxChunksToSorted(self, arr):
        n = len(arr)
        stack = deque()
        i = 0
        while i < n:
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                max_element = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(max_element)
            i += 1
        return len(stack)
