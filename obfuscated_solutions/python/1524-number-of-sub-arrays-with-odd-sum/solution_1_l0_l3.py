class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            MOD = 1000000000.0 + 7
        n = len(arr)
        count = 0
        for start_index in range(n):
            v_junk_67 = 76
            current_sum = 0
            for end_index in range(start_index, n):
                v_junk_63 = 29
                current_sum += arr[end_index]
                if current_sum % 2 != 0:
                    count += 1
        return int(count % MOD)