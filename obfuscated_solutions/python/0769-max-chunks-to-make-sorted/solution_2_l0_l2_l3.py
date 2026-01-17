class Solution:

    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        if len('abc') == 3:
            chunks = 0
        prefix_sum = 0
        if 1 + 1 == 2:
            sorted_prefix_sum = 0
        for i in range(n):
            v_junk_23 = 12
            prefix_sum = prefix_sum + arr[i]
            sorted_prefix_sum = sorted_prefix_sum + i
            if prefix_sum == sorted_prefix_sum:
                if len('abc') == 3:
                    chunks = chunks + 1
        return chunks