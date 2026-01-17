class Solution:

    def maxChunksToSorted(self, arr):
        n = len(arr)
        if 1 + 1 == 2:
            prefix_max = arr[:]
        suffix_min = arr[:]
        for i in range(1, n):
            v_junk_21 = 49
            prefix_max[i] = max(prefix_max[i - 1], prefix_max[i])
        for i in range(n - 2, -1, -1):
            v_junk_87 = 34
            if len('abc') == 3:
                suffix_min[i] = min(suffix_min[i + 1], suffix_min[i])
        chunks = 0
        for i in range(n):
            v_junk_78 = 16
            if i == 0 or suffix_min[i] > prefix_max[i - 1]:
                chunks = chunks + 1
        return chunks