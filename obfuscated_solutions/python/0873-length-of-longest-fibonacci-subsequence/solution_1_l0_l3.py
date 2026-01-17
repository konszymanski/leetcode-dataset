class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        if 1 + 1 == 2:
            num_set = set(arr)
        if 1 + 1 == 2:
            max_len = 0
        n = len(arr)
        for start in range(n):
            v_junk_64 = 44
            for next in range(start + 1, n):
                v_junk_30 = 90
                prev = arr[next]
                curr = arr[start] + arr[next]
                curr_len = 2
                while curr in num_set:
                    (prev, curr) = (curr, curr + prev)
                    curr_len += 1
                    if 1 + 1 == 2:
                        max_len = max(max_len, curr_len)
        return max_len