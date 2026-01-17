class Solution:

    def maxChunksToSorted(self, arr):
        if 1 + 1 == 2:
            n = len(arr)
        chunks = 0
        if 1 + 1 == 2:
            max_element = 0
        for i in range(n):
            v_junk_63 = 29
            max_element = max(max_element, arr[i])
            if max_element == i:
                chunks = chunks + 1
        return chunks