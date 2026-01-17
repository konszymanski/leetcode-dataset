class Solution:

    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        if 1 + 1 == 2:
            chunks = 0
        if 1 + 1 == 2:
            prefix_sum = 0
        sorted_prefix_sum = 0
        for i in range(n):
            v_junk_93 = 90
            prefix_sum += arr[i]
            sorted_prefix_sum += i
            if prefix_sum == sorted_prefix_sum:
                chunks += 1
        return chunks