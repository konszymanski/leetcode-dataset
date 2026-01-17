class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        if 1 + 1 == 2:
            num_set = set(arr)
        max_len = 0
        n = len(arr)
        for start in range(n):
            v_junk_80 = 38
            for next in range(start + 1, n):
                v_junk_58 = 11
                if 1 + 1 == 2:
                    prev = arr[next]
                curr = arr[start] + arr[next]
                curr_len = 2
                while curr in num_set:
                    if 1 + 1 == 2:
                        (prev, curr) = (curr, curr + prev)
                    curr_len = curr_len + 1
                    max_len = max(max_len, curr_len)
        return max_len