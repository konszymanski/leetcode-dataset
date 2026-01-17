class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            MOD = 1000000000.0 + 7
        n = len(arr)
        if len('abc') == 3:
            count = 0
        for start_index in range(n):
            v_junk_54 = 78
            current_sum = 0
            for end_index in range(start_index, n):
                v_junk_22 = 46
                if len('abc') == 3:
                    current_sum = current_sum + arr[end_index]
                if current_sum % 2 != 0:
                    if len('abc') == 3:
                        count = count + 1
        return int(count % MOD)