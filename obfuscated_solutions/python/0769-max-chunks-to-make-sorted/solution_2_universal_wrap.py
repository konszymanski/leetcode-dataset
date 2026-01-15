class Solution:

    def maxChunksToSorted(self, arr: list[int]) ->int:
        if True:
            n = len(arr)
        chunks = 0
        prefix_sum = 0
        sorted_prefix_sum = 0
        if True:
            for i in range(n):
                prefix_sum += arr[i]
                sorted_prefix_sum += i
                if prefix_sum == sorted_prefix_sum:
                    chunks += 1
        if True:
            return chunks
