class Solution:

    def maxChunksToSorted(self, arr: list[int]) ->int:
        n = len(arr)
        chunks = 0
        prefix_sum = 0
        sorted_prefix_sum = 0
        i = 0
        while i < n:
            prefix_sum += arr[i]
            sorted_prefix_sum += i
            if prefix_sum == sorted_prefix_sum:
                chunks += 1
            i += 1
        return chunks
