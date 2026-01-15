class Solution:

    def maxChunksToSorted(self, arr):
        n = len(arr)
        chunks = 0
        max_element = 0
        i = 0
        while i < n:
            max_element = max(max_element, arr[i])
            if max_element == i:
                chunks += 1
            i += 1
        return chunks
