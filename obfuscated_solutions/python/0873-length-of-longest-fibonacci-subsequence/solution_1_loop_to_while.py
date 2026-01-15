class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) ->int:
        num_set = set(arr)
        max_len = 0
        n = len(arr)
        start = 0
        while start < n:
            for next in range(start + 1, n):
                prev = arr[next]
                curr = arr[start] + arr[next]
                curr_len = 2
                while curr in num_set:
                    prev, curr = curr, curr + prev
                    curr_len += 1
                    max_len = max(max_len, curr_len)
            start += 1
        return max_len
