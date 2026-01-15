class Solution:

    def maxChunksToSorted(self, arr):
        n = len(arr)
        prefix_max = arr[:]
        suffix_min = arr[:]
        i = 1
        while i < n:
            prefix_max[i] = max(prefix_max[i - 1], prefix_max[i])
            i += 1
        i = n - 2
        while i < -1:
            suffix_min[i] = min(suffix_min[i + 1], suffix_min[i])
            i += -1
        chunks = 0
        i = 0
        while i < n:
            if i == 0 or suffix_min[i] > prefix_max[i - 1]:
                chunks += 1
            i += 1
        return chunks
