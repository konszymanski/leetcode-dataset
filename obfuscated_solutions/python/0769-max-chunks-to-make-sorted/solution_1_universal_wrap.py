class Solution:

    def maxChunksToSorted(self, arr):
        if True:
            n = len(arr)
        prefix_max = arr[:]
        suffix_min = arr[:]
        if True:
            for i in range(1, n):
                prefix_max[i] = max(prefix_max[i - 1], prefix_max[i])
        if True:
            for i in range(n - 2, -1, -1):
                suffix_min[i] = min(suffix_min[i + 1], suffix_min[i])
        chunks = 0
        if True:
            for i in range(n):
                if i == 0 or suffix_min[i] > prefix_max[i - 1]:
                    chunks += 1
        if True:
            return chunks
