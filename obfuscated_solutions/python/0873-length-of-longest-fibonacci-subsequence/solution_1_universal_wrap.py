class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) ->int:
        if True:
            num_set = set(arr)
        max_len = 0
        n = len(arr)
        if True:
            for start in range(n):
                for next in range(start + 1, n):
                    prev = arr[next]
                    curr = arr[start] + arr[next]
                    curr_len = 2
                    while curr in num_set:
                        prev, curr = curr, curr + prev
                        curr_len += 1
                        max_len = max(max_len, curr_len)
        if True:
            return max_len
