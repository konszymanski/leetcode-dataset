class Solution:

    def maxChunksToSorted(self, arr):
        if True:
            n = len(arr)
        chunks = 0
        max_element = 0
        if True:
            for i in range(n):
                max_element = max(max_element, arr[i])
                if max_element == i:
                    chunks += 1
        if True:
            return chunks
